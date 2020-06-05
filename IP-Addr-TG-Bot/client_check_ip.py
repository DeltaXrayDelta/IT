import urllib.request, os, json, time, re

os.environ['TZ'] = 'Asia/Shanghai'     # Timezone Name "Asia/Shanghai" "America/New_York"
current_dir_path = os.path.abspath(os.path.dirname(__file__))
create_new_file = False
msg = "empty"

request = urllib.request.Request(
    url='https://ip.istatmenus.app',
    headers={
        'User-Agent': 'iStat%20Menus%20Status/1116 CFNetwork/1126 Darwin/19.5.0 (x86_64)',
    }
    )
current_ip = urllib.request.urlopen(request).read().decode('utf8')

regex_pattern = r'[0-9]+(?:\.[0-9]+){3}'
if not len(re.findall(regex_pattern, current_ip)): 
    current_ip = 'Error: IP Address Format Mismatch: {}'.format(current_ip)
# print('Current IP = ', current_ip)

if os.path.exists(os.path.join(current_dir_path, 'current_ip.json')):
    original_ip = json.load(open(os.path.join(current_dir_path, 'current_ip.json')))['current_ip']
    # print('Original IP = ', original_ip)
else: 
    msg = 'File does not exist, will create a new file'
    # print(msg)
    original_ip = current_ip
    create_new_file = True

ip_changed = (current_ip != original_ip)

if ip_changed:
    msg = 'Public IP Changed: {} => {}'.format(original_ip, current_ip)
    # print(msg)

if ip_changed or create_new_file:
# if True:
    with open(os.path.join(current_dir_path, 'current_ip.json'), 'w') as file:
        file.write(json.dumps({
            'current_ip': current_ip, 
            'message': msg,
            'update_time': time.strftime("%Y-%m-%d %H:%M:%S"),
            'timestamp': int(time.time()),
            }))