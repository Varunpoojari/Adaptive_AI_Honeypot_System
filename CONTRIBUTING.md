# Contributing to Adaptive AI Honeypot System

Thanks for your interest in improving this project. Bug reports, documentation fixes and focused feature work are all welcome.

## Ground rules

- This is a **defensive** research tool. Contributions must support threat intelligence, detection or deception research, not offensive use.
- Never test against systems you do not own or have permission to use.
- Never expose the honeypot directly to the internet while developing.

## Reporting bugs and ideas

1. Search the existing [issues](https://github.com/Varunpoojari/Adaptive_AI_Honeypot_System/issues) first.
2. Open a new issue with the steps to reproduce, what you expected, what happened, and your Python and OS versions.
3. For security problems, follow [SECURITY.md](SECURITY.md) instead of opening a public issue.

## Development setup

Requires Python 3.8+ and, optionally, Docker.

```bash
git clone https://github.com/Varunpoojari/Adaptive_AI_Honeypot_System.git
cd Adaptive_AI_Honeypot_System
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run the honeypot locally:

```bash
PYTHONPATH=$PYTHONPATH:. python3 src/core/honeypot.py
```

## Pull request process

1. Fork the repository and create a branch from `main` (for example `fix/log-rotation` or `docs/clarify-config`).
2. Keep each pull request to one change so it is easy to review.
3. Follow the existing style in `src/`: PEP 8, clear names, and docstrings for public functions.
4. Update the README or `docs/` when behaviour or configuration changes.
5. Describe what changed, why, and how you checked it in the pull request description.

## Code style

- PEP 8, four-space indentation, lines under about 100 characters.
- Prefer small functions with a single purpose.
- Do not commit secrets, captured attacker data, or log files.

## License

By contributing you agree that your contributions are licensed under the project's [MIT License](LICENSE).
