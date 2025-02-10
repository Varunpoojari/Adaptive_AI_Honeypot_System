# Adaptive AI Honeypot System

An intelligent honeypot system that uses machine learning to adapt to attacker behavior and generate actionable threat intelligence.

## Features

- **Deception Engine**: Randomizes open ports, fake vulnerabilities, and mimics services
- **Behavioral Profiling**: Uses ML to classify attackers based on interaction patterns
- **Threat Intelligence**: Generates IoCs and integrates with MITRE ATT&CK Framework
- **Adaptive Responses**: Uses reinforcement learning to improve deception strategies

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Varunpoojari/adaptive-ai-honeypot.git
cd adaptive-ai-honeypot
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the honeypot:
```bash
PYTHONPATH=$PYTHONPATH:. python3 src/core/honeypot.py
```

The honeypot will start listening on ports 21 (FTP), 22 (SSH), 80 (HTTP), and 443 (HTTPS).

## Architecture

- `src/core/`: Core honeypot functionality
- `src/utils/`: Utility functions and logging
- `src/ml/`: Machine learning components

## Security Warning

This is a security tool that should only be deployed in controlled environments. Never expose it directly to the internet without proper security measures in place.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

MIT License