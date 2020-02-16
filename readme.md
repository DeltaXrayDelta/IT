# Internet / IT / Hardware

- [Public DNS Service](#public-dns-service)
  * [Global](#global)
  * [Mainland China](#mainland-china)
- [Windows](#windows)
  * [Set Wi-Fi Priority in Windows 10](#set-wi-fi-priority-in-windows-10)
- [macOS](#macos)
  * [Disable System Update Notification Badge on System Preferences Icon](#disable-system-update-notification-badge-on-system-preferences-icon)
  * [Clear Calender.app Timezone List](#clear-calenderapp-timezone-list)
- [CentOS](#centos)
  * [Task Manager (Show PID)](#task-manager-show-pid-)
  * [Kill Process by PID](#kill-process-by-pid)

## Public DNS Service

### Global

Service Provider | URL | Notes
---------|----------|---------
Cloudflare | [https://cloudflare-dns.com/dns-query](https://cloudflare-dns.com/dns-query) <br> [https://mozilla.cloudflare-dns.com/dns-query](https://mozilla.cloudflare-dns.com/dns-query) <br> [1.1.1.1](1.1.1.1) <br> [1.0.0.1](1.0.0.1) | 
Google | [https://dns.google/dns-query](https://dns.google/dns-query) <br> [8.8.8.8](8.8.8.8) <br> [8.8.4.4](8.8.4.4) | 
ADGuard | [https://dns.adguard.com/dns-query](https://dns.adguard.com/dns-query) <br> [176.103.130.130](176.103.130.130) <br> [176.103.130.131](176.103.130.131) | 

### Mainland China

Service Provider | URL | Notes
---------|----------|---------
114 DNS | [114.114.114.114](114.114.114.114) <br> [114.114.115.115](114.114.115.115) | 
Alibaba | [223.5.5.5](223.5.5.5) <br> [223.6.6.6](223.6.6.6)| 
CNNIC | [1.2.4.8](1.2.4.8) <br> [210.2.4.8](210.2.4.8) | 
China Telecom <br> Guangdong | [202.96.128.86](202.96.128.86) <br> [202.96.134.33](202.96.134.33) | 

## Windows

### Set Wi-Fi Priority in Windows 10

Run command line (CMD) as admin

Get a list of saved networks
```
netsh wlan show profiles
```
Get interface name
```
netsh wlan show interfaces
```
Set your preferred network as first priority
```
netsh wlan set profileorder name="<YOUR WI-FI SSID>" interface="<YOUR INTERFACE NAME>" priority=1
```
## macOS

### Disable System Update Notification Badge on System Preferences Icon
```
defaults write com.apple.systempreferences AttentionPrefBundleIDs 0; killall Dock
```
### Clear Calender.app Timezone List
```
defaults delete com.apple.iCal 'RecentlyUsedTimeZones'
```

## CentOS

### Task Manager (Show PID)
```
ps -aux
```
### Kill Process by PID
```
kill <PID>
```