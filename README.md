
# Directory Fuzzer 🔍

A lightweight web directory discovery tool written in Python, designed for reconnaissance and security auditing. It rapidly probes target URLs using a built-in wordlist to find hidden administrative paths, backup files, and restricted endpoints.

## Features 🚀
* **Path Discovery**: Iterates through common web directories and sensitive files (e.g., admin panels, configuration files, `.git` directories).
* **Smart HTTP Status Filtration**: Automatically filters out dead links and highlights active resources (`200 OK`, `301/302 Redirects`, and `403 Forbidden`).
* **Rich CLI Visualization**: Leverages the `rich` library to render color-coded, clean terminal tables.)


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
