import socket
import threading
import json
from datetime import datetime
import sys
from src.utils.logger import HoneypotLogger

class Honeypot:
    def __init__(self, host='0.0.0.0', ports=[21, 22, 80, 443]):
        self.host = host
        self.ports = ports
        self.active_connections = {}
        self.logger = HoneypotLogger()
        self.running = True
        
        # Define basic service responses
        self.service_responses = {
            21: "220 FTP server ready\r\n",
            22: "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1\r\n",
            80: "HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\n\r\n",
            443: "HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\n\r\n"
        }

    def start_service(self, port):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((self.host, port))
            server.listen(5)
            
            self.logger.log_connection("SERVER", port, f"Started honeypot service on port {port}")
            
            while self.running:
                try:
                    client, address = server.accept()
                    client_handler = threading.Thread(
                        target=self.handle_connection,
                        args=(client, address, port)
                    )
                    client_handler.start()
                except Exception as e:
                    self.logger.log_error(f"Error accepting connection on port {port}: {str(e)}")
                    
        except Exception as e:
            self.logger.log_error(f"Error starting service on port {port}: {str(e)}")
        finally:
            server.close()

    def handle_connection(self, client_socket, address, port):
        ip = address[0]
        self.logger.log_connection(ip, port)
        
        try:
            if port in self.service_responses:
                client_socket.send(self.service_responses[port].encode())
            
            while self.running:
                try:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                        
                    decoded_data = data.decode('utf-8', errors='ignore').strip()
                    self.logger.log_connection(ip, port, decoded_data)
                    
                    if port in self.service_responses:
                        client_socket.send(self.service_responses[port].encode())
                        
                except socket.timeout:
                    continue
                except Exception as e:
                    self.logger.log_error(f"Error receiving data from {ip}:{port} - {str(e)}")
                    break
                    
        except Exception as e:
            self.logger.log_error(f"Error handling connection from {ip}:{port} - {str(e)}")
        finally:
            client_socket.close()

    def start(self):
        self.logger.log_connection("SERVER", 0, "Starting honeypot...")
        
        threads = []
        for port in self.ports:
            thread = threading.Thread(target=self.start_service, args=(port,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
            
        try:
            while True:
                for thread in threads:
                    if not thread.is_alive():
                        self.logger.log_error("A service thread has died. Restarting honeypot...")
                        self.restart()
                        break
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.running = False
        self.logger.log_connection("SERVER", 0, "Stopping honeypot...")

    def restart(self):
        self.stop()
        self.running = True
        self.start()

if __name__ == "__main__":
    honeypot = Honeypot()
    honeypot.start()