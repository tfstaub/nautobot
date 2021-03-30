#!/bin/bash/env python3

import requests
import getpass

username = input("Username: ")
password = getpass()
site_name = input("What is the name of the site? ")
print("What is the current status?")
status_list = ['Active', 'Decommissioning', 'Planned', 'Retired', 'Staging']
print(f"Please choose from the following {status_list}.")
site_status = input()

site = {
    name: site_name,
    slug: site_name.lower(),
    status: site_status
}

result = requests.get(f"https://{nautobot}/api/site")
print(result)

requests.post(f"https://{nautobot}/api/site/")
