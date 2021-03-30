#!/bin/bash/env python3

import requests
#import getpass

#username = input("Username: ")
#password = getpass("Password: ")
nautobot = input("Server: ")
ip_address = input("IP Address:  ")
print("What is the current status?")
status_list = ['Active', 'DHCP', 'Deprecated', 'Reserved', 'SLAAC']
print(f"Please choose from the following {status_list}.")
ip_status = input()

requests.packages.urllib3.disable_warnings()

header = {
    "Accept": "application/json",
    "Authorization": " {{ Token }} "
}

body = {
    "address": ip_address,
    "status": ip_status
}

url = f"https://{nautobot}/api/ipam/ip-addresses/"

get_result = requests.get(url=url, headers=header, verify=False)
print(get_result)

post_result = requests.post(url=url, headers=header, data=body, verify=False)
print(post_result)
