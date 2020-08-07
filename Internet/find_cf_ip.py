import requests
import threadpool
from IPy import IP

def IP_Test(ip):
    try:
        r = requests.get('http://' + ip + '/', timeout=3)
        if 'Direct IP access not allowed' in r.text:
            print('可用:' + ip, flush=True)
        else:
            print('不可用:' + ip, flush=True)
    except requests.exceptions.ConnectionError:
        print('无服务:' + ip, flush=True)
    except requests.exceptions.ReadTimeout:
        print('无服务:' + ip, flush=True)


iplist = list()

ips = IP('173.245.48.0/20')
# ips = IP('103.21.244.0/22')
# ips = IP('103.22.200.0/22')
# ips = IP('103.31.4.0/22')
# ips = IP('141.101.64.0/18')
# ips = IP('108.162.192.0/18')
# ips = IP('190.93.240.0/20')
# ips = IP('188.114.96.0/20')
# ips = IP('197.234.240.0/22')
# ips = IP('198.41.128.0/17')
# ips = IP('162.158.0.0/15')
# ips = IP('104.16.0.0/12')
# ips = IP('172.64.0.0/13')
ips = IP('131.0.72.0/22')
for ip in ips:
    iplist.append(str(ip))

pool = threadpool.ThreadPool(100)  # 线程池设置,最多同时跑N个线程
tasks = threadpool.makeRequests(IP_Test, iplist)
[pool.putRequest(task) for task in tasks]
pool.wait()
