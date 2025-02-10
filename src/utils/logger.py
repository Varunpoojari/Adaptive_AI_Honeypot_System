import logging
from datetime import datetime
import os

class HoneypotLogger:
    def __init__(self, log_dir='logs'):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        self.log_file = os.path.join(log_dir, f'honeypot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger('honeypot')
    
    def log_connection(self, ip, port, data=None):
        message = f"Connection from {ip} on port {port}"
        if data:
            message += f" - Data: {data}"
        self.logger.info(message)
    
    def log_attack(self, ip, port, attack_type, payload=None):
        message = f"Attack detected - Type: {attack_type} from {ip} on port {port}"
        if payload:
            message += f" - Payload: {payload}"
        self.logger.warning(message)
    
    def log_error(self, error_msg):
        self.logger.error(error_msg)