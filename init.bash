if [ -d "/etc/pandora" ]; then
  exit 1 ; 
fi
mkdir /etc/pandora ; 
echo "{}" > /etc/pandora/v2ray_config.json ; 
echo "[]" > /etc/pandora/accounts.json ; 
echo '{"telegram_bot_token":"","expiration_check_interval":30}' > /etc/pandora/app_config.json ; 
