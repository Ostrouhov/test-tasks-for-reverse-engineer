import requests
from bs4 import BeautifulSoup

proxies = {
#     'http': 'http://BFMgbDhv:MHJKenKZ@193.150.170.23:62618',
#     'https': 'http://BFMgbDhv:MHJKenKZ@193.150.170.23:62618', (If needed)
}


ip_response = requests.get(url="https://2ip.ru/", proxies=proxies)
if ip_response.status_code == 200:
    ip_soup = BeautifulSoup(ip_response.text, 'html.parser')
    ip_address = ip_soup.find('div', class_='ip').get_text().strip()
    print(ip_address)
else:
    print(f"Request error: {ip_response.status_code}")


ip_zone_response = requests.get(url=f"https://ipinfo.io/{ip_address}/json", proxies=proxies)
ip_zone = ip_zone_response.json().get('timezone')
if ip_zone_response.status_code == 200:
    print(ip_zone)
else:
    print(f"Request error: {ip_zone_response.status_code}")


timezone_regions_response = requests.get(url="https://gist.github.com/salkar/19df1918ee2aed6669e2", proxies=proxies)
if timezone_regions_response.status_code == 200:
    timezone_regions_soup = BeautifulSoup(timezone_regions_response.text, 'html.parser')
    timezone_all_regions = timezone_regions_soup.find_all('tr')
    for reg in timezone_all_regions:
        if (reg.get_text().strip().__contains__(ip_zone)):
            with open("result.txt", "a") as file:
                file.write(reg.get_text().strip())
            print(reg.get_text().strip())
else:
    print(f"Request error: {timezone_regions_response.status_code}")