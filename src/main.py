'''
    @Author : Swornim Shrestha
    @Username: swornim00
    @Email: srestaswrnm@gmail.com
    @Date: July 3, 2019 6:07 PM [Kathmandu Time Zone]

    MIT License

    Copyright (c) 2019 Swornim Shrestha

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
'''


import requests,sys,re
from bs4 import BeautifulSoup


def banner():
    banner = '''
    @Author : Swornim Shrestha
    @Username: swornim00
    @Email: srestaswrnm@gmail.com
    @Date: July 3, 2019 6:07 PM [Kathmandu Time Zone]

    Copyright (c) 2019 Swornim Shrestha
    '''
    print(banner)
    
def guide():
    print('''
    How to use: 

    python3 whois-np.py <domain name>
    Example: python3 whois-np.py swornimshrestha.com.np\n\n''')

def handle_arguments():
    args = sys.argv
    length = len(args)
    if length ==1:
        print("[!] Arguments needed")
        guide()
    else:
        if(args[1] == "help"):
            guide()
        else:
            domainName = args[1]
            return domainName

    return 0

def available():
    print("Wo Hoo!! The Domain Name is available")

def display_details(whois_soup):
    row_all = whois_soup.find_all('tr')
    for row in row_all:
        print(row.find_all('td')[0].text ,row.find_all('td')[1].text)

def load_config():
    whois_domain_url = "https://register.com.np/whois-lookup"
    return whois_domain_url


def main(domainName):
    session_req = requests.Session()
    web_data = session_req.get(whois_domain_url)
    web_soup = BeautifulSoup(web_data.text,'html.parser')

    _token = web_soup.find("input",{"name":"_token"})['value']
    _action = web_soup.find("form")['action']
    form_data = dict(domainName='swornimshrestha',domainExtension='.com.np',_token=_token)
    whois_detail = requests.post(_action,data=form_data, headers=dict(Referrer=whois_domain_url),cookies=dict(web_data.cookies))

    whois_soup = BeautifulSoup(whois_detail.text,'html.parser')

    check = whois_soup.find(class_="available")

    if(check):
        available()



if __name__ =="__main__":
    whois_domain_url= load_config()
    banner()
    domainName= handle_arguments()
    main(domainName)