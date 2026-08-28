import sys
import argparse
import requests
from rich.console import Console
from rich.table import Table

console = Console()

# Built-in mini wordlist of common administrative and sensitive paths
DEFAULT_WORDS = [
    "admin", "administrator", "login", "dashboard", "api", 
    "config", "backup", "db", "server-status", ".git", 
    "secret", "test", "uploads", "wp-login.php"
]

def fuzz_directory(target_url, wordlist):
    """Iterates through a list of paths and tests for valid HTTP responses."""
    results = []
    base_url = target_url.rstrip("/")
    
    for word in wordlist:
        url = f"{base_url}/{word}"
        try:
            response = requests.get(url, timeout=5, allow_redirects=False)
            status_code = response.status_code
            
            # Filter for interesting or active web paths
            if status_code in [200, 301, 302, 403]:
                results.append((url, status_code))
        except requests.exceptions.RequestException:
            pass
            
    return results

def main():
    parser = argparse.ArgumentParser(description="Lightweight Directory Fuzzer for Web Reconnaissance")
    parser.add_argument("url", help="Target base URL (e.g., https://example.com)")
    args = parser.parse_args()

    console.print(f"[bold cyan][+] Starting directory fuzzing on:[/bold cyan] {args.url}")

    with console.status("[bold green]Probing target paths..."):
        discovered = fuzz_directory(args.url, DEFAULT_WORDS)

    if discovered:
        table = Table(title="Discovered Endpoints")
        table.add_column("Endpoint URL", style="bold cyan")
        table.add_column("Status Code", style="bold")

        for url, status in discovered:
            # Color-code status codes for quick triage
            color = "green" if status == 200 else "yellow" if status in [301, 302] else "red"
            table.add_row(url, f"[{color}]{status}[/{color}]")

        console.print(table)
    else:
        console.print("[bold yellow][-] No common paths found with the default wordlist.[/bold yellow]")

if __name__ == "__main__":
    main()
