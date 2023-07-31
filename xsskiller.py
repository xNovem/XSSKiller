import os
import requests
from bs4 import BeautifulSoup

def display_banner():
    banner_text = """
__  ______ ____    _  ___ _ _
\ \/ / ___/ ___|  | |/ (_) | | ___ _ __
 \  /\___ \___ \  | ' /| | | |/ _ \ '__|
 /  \ ___) |__) | | . \| | | |  __/ |
/_/\_\____/____/  |_|\_\_|_|_|\___|_|
                                   
    """
    version = "\033[1;31mV1.0\033[0m"
    print("\033[1;31m" + banner_text + "\033[0m" + " " + version)

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
    site_url = input("Lutfen kontrol etmek istediginiz siteyi girin: ")
    check_xss_vulnerability(site_url)

if __name__ == "__main__":
    main()
