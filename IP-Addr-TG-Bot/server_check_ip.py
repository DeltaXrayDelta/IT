import json

def main_public_ip():
    ip_addr_json = json.load(open('/YOUR_PATH/current_ip.json'))

    msg = ''
    msg += (ip_addr_json['update_time'] + '\n')
    msg += (ip_addr_json['current_ip'] + '\n')
    msg += (ip_addr_json['message'] + '\n')
    return msg

if __name__ == "__main__":
    print(main_public_ip())