import os
import requests
from bs4 import BeautifulSoup

def display_banner():
    banner_text = r"""
   ____  _              _  __     __       
  / ___|| |_   _  ___  | | \ \   / /__  ___
 | |  _ | | | | |/ _ \ | |  \ \ / / _ \/ __|
 | |_| || | |_| |  __/ | |___\ V /  __/\__ \
  \____||_|\__,_|\___| |______\_/ \___||___/
                     XSS Killer
    """
    version = "v1.1"
    print("\033[1;33m" + banner_text + "\033[0m")
    print(f"Version: {version}\n")

def check_xss_vulnerability(site_url):
    response = requests.get(site_url)
    soup = BeautifulSoup(response.text, "html.parser")
    script_tags = soup.find_all("script")
    if script_tags:
        print("\033[1;32mXSS zafiyeti tespit edildi!\033[0m")
        for i, tag in enumerate(script_tags, start=1):
            print(f"{i}. <script> etiketi: {tag}")
    else:
        print("\033[1;31mXSS zafiyeti tespit edilemedi.\033[0m")

def main():
    display_banner()
    site_url = input("Lütfen kontrol etmek istediğiniz siteyi girin: ")
    check_xss_vulnerability(site_url)

if __name__ == "__main__":
    main()
  
