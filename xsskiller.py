import os
import requests
from HTMLParser import HTMLParser

class XSSParser(HTMLParser):
    def __init__(self):
        self.xss_found = False
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.xss_found = True

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
    parser = XSSParser()
    parser.feed(response.text)
    if parser.xss_found:
        print("\033[1;32mXSS zafiyeti tespit edildi!\033[0m")
    else:
        print("\033[1;31mXSS zafiyeti tespit edilemedi.\033[0m")

def main():
    display_banner()
    site_url = raw_input("Lutfen kontrol etmek istediginiz siteyi girin: ")
    check_xss_vulnerability(site_url)

if __name__ == "__main__":
    main()
    
