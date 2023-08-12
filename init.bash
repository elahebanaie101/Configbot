if [ -d "/etc/pandora" ]; then
  exit 1 ; 
fi
mkdir /etc/pandora ; 
cp v2ray-linux-64/vpoint_vmess_freedom.json /etc/pandora/v2ray_config.json ; 
echo "[]" > /etc/pandora/accounts.json ; 
echo '{"telegram_bot_token":"","expiration_check_interval":30}' > /etc/pandora/app_config.json ; 
