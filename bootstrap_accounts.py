import json 
fp = open("uuid_list.txt", "r+")
uuids = fp.readlines()
uuids = list(map(lambda x:x[:-1] , uuids))
handle = open("/etc/pandora/accounts.json", "w+")
accounts = []
client_config_template = '{"dns":{"hosts":{"domain:googleapis.cn":"googleapis.com"},"servers":["8.8.8.8"]},"inbounds":[{"listen":"127.0.0.1","port":10808,"protocol":"socks","settings":{"auth":"noauth","udp":true,"userLevel":8},"sniffing":{"destOverride":["http","tls"],"enabled":true},"tag":"socks"},{"listen":"127.0.0.1","port":10809,"protocol":"http","settings":{"userLevel":8},"tag":"http"},{"listen":"127.0.0.1","port":10853,"protocol":"dokodemo-door","settings":{"address":"8.8.8.8","network":"tcp,udp","port":53},"tag":"dns-in"}],"log":{"loglevel":"warning"},"outbounds":[{"mux":{"concurrency":8,"enabled":false},"protocol":"vmess","settings":{"vnext":[{"address":"65.108.56.176","port":10086,"users":[{"alterId":64,"encryption":"","flow":"","id":"23ad6b10-8d1a-40f7-8ad0-e3e35cd38297","level":8,"security":"none"}]}]},"streamSettings":{"network":"tcp","security":"","tcpSettings":{"header":{"type":"none"}}},"tag":"proxy"},{"protocol":"freedom","settings":{},"tag":"direct"},{"protocol":"blackhole","settings":{"response":{"type":"http"}},"tag":"block"},{"protocol":"dns","tag":"dns-out"}],"routing":{"domainStrategy":"AsIs","rules":[{"inboundTag":["dns-in"],"outboundTag":"dns-out","type":"field"},{"ip":["8.8.8.8"],"outboundTag":"proxy","port":"53","type":"field"}]}}'
for uuid in uuids :
    accounts.append({"uuid":uuid ,"id" : uuid , "alterId" : 4 , "level" : 0 ,  "config_link" : f"vmess://{uuid}@65.108.56.176:10086?path=/&security=none&encryption=none#pandora_config"})
json.dump(accounts , handle)

v2ray_config_fp = open('/etc/pandora/v2ray_config.json','r')
v2ray_config = json.load(v2ray_config_fp)
if not 'settings' in v2ray_config['inbounds'] : 
    v2ray_config['inbounds']['settings'] = {}
if not 'clients' in v2ray_config['inbounds']['settings'] : 
    v2ray_config['inbounds']['settings']['clients'] = []

v2ray_config['inbounds']['settings']['clients'] = accounts 
v2ray_config_fp.close()

json.dump(v2ray_config , open('/etc/pandora/v2ray_config.json','w'))