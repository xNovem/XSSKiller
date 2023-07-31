# -*- coding: utf-8 -*-
import os
import requests
import re

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
    if re.search(r"<script>", response.text):
        print("\033[1;32mXSS zafiyeti tespit edildi!\033[0m")
        scripts = re.findall(r"<script>.*?</script>", response.text, re.DOTALL)
        i = 1
        for script in scripts:
            print("%d. <script> etiketi: %s" % (i, script))
            i += 1
    else:
        print("\033[1;31mXSS zafiyeti tespit edilemedi.\033[0m")

def main():
    display_banner()
    site_url = raw_input("Lutfen kontrol etmek istediginiz siteyi girin: ")
    check_xss_vulnerability(site_url)

if __name__ == "__main__":
    main()
