# Deployment Guide

## Table of Contents
- [Environment Setup](#environment-setup)
- [Installation](#installation)
- [Configuration](#configuration)
- [Docker Deployment](#docker-deployment)
- [Monitoring](#monitoring)
- [Maintenance](#maintenance)

## Environment Setup

### System Requirements
- Linux/Unix-based system (Ubuntu 20.04+ recommended)
- Python 3.8+
- Docker 20.10+
- 4GB RAM minimum
- 20GB storage

### Network Requirements
- Dedicated network interface
- Isolated network segment
- Firewall access for specified ports

## Installation

### 1. Base System Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3-pip python3-venv docker.io

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker
```

### 2. Project Setup
```bash
# Clone repository
git clone https://github.com/Varunpoojari/adaptive-ai-honeypot.git
cd adaptive-ai-honeypot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Configuration

### 1. Basic Configuration
Edit `config/honeypot.yaml`:

```yaml
honeypot:
  host: '0.0.0.0'
  ports:
    - 21  # FTP
    - 22  # SSH
    - 80  # HTTP
    - 443 # HTTPS
  
  logging:
    level: INFO
    directory: '/var/log/honeypot'
    rotation: '1 day'
    
  security:
    max_connections: 1000
    timeout: 300
    banned_ips: []
```

### 2. Service Configuration
Edit `config/services.yaml`:

```yaml
services:
  ftp:
    banner: '220 FTP server ready'
    auth_required: true
    
  ssh:
    banner: 'SSH-2.0-OpenSSH_8.2p1'
    auth_required: true
    
  http:
    response_code: 200
    server: 'Apache/2.4.41'
```

## Docker Deployment

### 1. Build Docker Image
```bash
docker build -t honeypot:latest .
```

### 2. Run Container
```bash
docker run -d \
  --name honeypot \
  --restart unless-stopped \
  -p 21:21 -p 22:22 -p 80:80 -p 443:443 \
  -v /var/log/honeypot:/app/logs \
  honeypot:latest
```

### 3. Container Management
```bash
# Check container status
docker ps -a | grep honeypot

# View logs
docker logs -f honeypot

# Stop container
docker stop honeypot

# Start container
docker start honeypot
```

## Monitoring

### 1. Log Monitoring
```bash
# Real-time log viewing
tail -f /var/log/honeypot/honeypot.log

# Search for specific attacks
grep "Attack detected" /var/log/honeypot/honeypot.log
```

### 2. System Monitoring
```bash
# Check resource usage
docker stats honeypot

# Monitor network connections
netstat -tuln | grep -E ':(21|22|80|443)'
```

### 3. Alert Setup
Configure alert thresholds in `config/alerts.yaml`:

```yaml
alerts:
  email:
    enabled: true
    recipients: ['security@example.com']
    
  thresholds:
    connections_per_minute: 100
    failed_auth_attempts: 10
    data_transfer_mb: 50
```

## Maintenance

### 1. Backup Configuration
```bash
# Backup logs and configuration
tar -czf honeypot-backup-$(date +%Y%m%d).tar.gz \
  /var/log/honeypot \
  /path/to/config/*.yaml
```

### 2. Updates
```bash
# Pull latest code
git pull origin main

# Rebuild Docker image
docker build -t honeypot:latest .

# Restart container
docker restart honeypot
```

### 3. Health Checks
Regular health checks to perform:
- Monitor system resources
- Check log rotation
- Verify data collection
- Test alert system
- Update banned IP list

## Troubleshooting

### Common Issues

1. **Connection Issues**
```bash
# Check if ports are open
sudo lsof -i -P -n | grep LISTEN

# Verify Docker networking
docker network inspect bridge
```

2. **Performance Issues**
```bash
# Check system resources
top -p $(pgrep -f honeypot)

# Monitor I/O
iostat -x 1
```

3. **Log Issues**
```bash
# Check disk space
df -h

# Verify log permissions
ls -l /var/log/honeypot
```

## Security Recommendations

1. **Network Security**
   - Use dedicated network interface
   - Implement network segmentation
   - Regular security audits

2. **Access Control**
   - Limit SSH access
   - Use strong passwords
   - Implement 2FA

3. **Monitoring**
   - Set up external monitoring
   - Configure alerts
   - Regular log analysis

## Support

For issues and support:
1. Check the [troubleshooting guide](#troubleshooting)
2. Review [GitHub Issues](https://github.com/Varunpoojari/adaptive-ai-honeypot/issues)
3. Open a new issue if needed

---

Remember to check for updates to this guide in the repository.