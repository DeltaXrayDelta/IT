import requests
s_line = "-" * 40
mac_addr = input("Enter MAC Address => ")
url_api = "https://api.macvendors.com/" + mac_addr
manufact = requests.get(url_api).text
print(s_line,mac_addr,manufact,s_line,sep="\n")