# Security Policy

The Adaptive AI Honeypot System deliberately accepts hostile traffic and runs service emulators, so it needs careful handling. Please treat everything it captures as untrusted.

## Supported versions

| Version | Supported |
|---|---|
| `main` | Yes |
| Older commits | No |

## Reporting a vulnerability

Please **do not open a public issue** for security problems.

Report privately through GitHub's [private vulnerability reporting](https://github.com/Varunpoojari/Adaptive_AI_Honeypot_System/security/advisories/new) (Security tab, then "Report a vulnerability").

Please include:

- what is affected (a file, service emulator or configuration option)
- steps to reproduce, with a minimal example if possible
- the impact you expect (for example container escape, log injection, or a crash from crafted input)

I aim to acknowledge reports within 7 days and to agree a fix and disclosure timeline with you before anything is made public.

## Scope

In scope:

- the honeypot core and service emulation code in `src/`
- how captured attacker input is logged, parsed and fed to the ML components
- the provided `Dockerfile` and default configuration

Out of scope:

- vulnerabilities in third-party dependencies (please report those upstream)
- the behaviour of attackers the honeypot is designed to attract
- findings that need an already-compromised host

## Safe deployment

- Never expose the honeypot directly to the internet.
- Run it in an isolated container or VM with resource limits and no access to production networks.
- Treat captured payloads, logs and attacker input as hostile: do not open or execute them on a normal workstation.
- Keep dependencies up to date.
