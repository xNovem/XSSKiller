import os
import requests

def display_banner():
    banner_text = """
  ____  _              _  __     __       
 / ___|| |_   _  ___  | | \ \   / /__  ___
| |  _ | | | | |/ _ \ | |  \ \ / / _ \/ __|
| |_| || | |_| |  __/ | |___\ V /  __/\__ \\
 \____||_|\__,_|\___| |______\_/ \___||___/
                     XSS Killer
    """
    version = "\033[1;31mV1.0\033[0m"
    print("\033[1;31m" + banner_text + "\033[0m" + " " + version)

def check_xss_vulnerability(site_url):
    response = requests.get(site_url)
    if "<script>" in response.text:
        print("\033[1;32mXSS zafiyeti tespit edildi!\033[0m")
    else:
        print("\033[1;31mXSS zafiyeti tespit edilemedi.\033[0m")

def main():
    display_banner()
    site_url = raw_input("Lutfen kontrol etmek istediginiz siteyi girin: ")
    check_xss_vulnerability(site_url)

if __name__ == "__main__":
    main()
