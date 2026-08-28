# Sec-Scanner & Recon Suite 🛡️

A lightweight, modular cybersecurity reconnaissance and web auditing tool written in Python. Designed and tested to run natively on mobile environments (iOS via iSH Terminal) and standard desktop systems.

## Features 🚀
* **HTTP Header Security Audit**: Scans target URLs for critical security headers (HSTS, CSP, X-Frame-Options, etc.) to evaluate browser-side hardening.
* **SSL/TLS Certificate Inspection**: Analyzes cryptographic validity, issuer information, and expiration timelines with automated day-tracking alerts.
* **Directory Fuzzer**: Probes target web applications against common administrative paths and hidden files using multi-threaded or iterative request filtering.
* **Rich CLI Interface**: Utilizes the `rich` library for high-contrast, terminal-rendered status tables and indicators.

## Installation & Setup 📦

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/sirtruth/Sec-Scanner.git](https://github.com/sirtruth/Sec-Scanner.git)
   cd Sec-Scanner
