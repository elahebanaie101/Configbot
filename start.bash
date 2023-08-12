chmod +x ./v2ray-linux-64/v2ray;
./v2ray-linux-64/v2ray -c /etc/pandora/v2ray_config.json; 
echo $! > /etc/pandora/running_pgid.txt;
