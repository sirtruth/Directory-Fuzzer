# Directory Fuzzer🛡️

A lightweight, modular cybersecurity reconnaissance and web auditing tool written in Python. Designed and tested to run natively on mobile environments (iOS via iSH Terminal) and standard desktop systems.

## Features 🚀
* **HTTP Header Security Audit**: Scans target URLs for critical security headers (HSTS, CSP, X-Frame-Options, etc.) to evaluate browser-side hardening.
* **SSL/TLS Certificate Inspection**: Analyzes cryptographic validity, issuer information, and expiration timelines with automated day-tracking alerts.
* **Directory Fuzzer**: Probes target web applications against common administrative paths and hidden files using multi-threaded or iterative request filtering.
* **Rich CLI Interface**: Utilizes the `rich` library for high-contrast, terminal-rendered status tables and indicators.

## Installation & Setup 📦

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/sirtruth/dir-fuzzer.git](https://github.com/sirtruth/dir-fuzzer.git)
   cd dir-fuzzer
2. **Install dependencies**:
    pip install requests rich

   **Usage 💻**

 **Probe for hidden administrative endpoints or configuration files:**

python3 dir_fuzzer.py [https://example.com](https://example.com)

    **Requirements ⚙️**

 *Python 3.8+*

 ⁠*requests⁠*

 ⁠*rich⁠*

    **Disclaimer ⚠️
This tool is created strictly for educational purposes, portfolio demonstration, and authorized security assessments. Only run scans against targets you own or have explicit written permission to test.**
