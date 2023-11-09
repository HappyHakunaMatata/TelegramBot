# TelegramBot
Django Telegram bot

Installation
1. git clone https://github.com/HappyHakunaMatata/TelegramBot.git and mount the folder via "cd /your_path"
2. Specify all commands in .env file in /TelegramBot/TelegramBot/.env:
Example of .env:
   telegram_token="00000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAA"
   channel_link="https://t.me/SOMETHINGHERE"	 
   public_chat_id="-10000000000000" 
   session_name="0000-0000-0000-0002" 
   api_id=00000000
   api_hash="0a0a0a0a0a0a0a0a0a0a0a0a0a0" 
   phone_number="+00000000000" 
   bitrix24_api="https://SOMETHINGHERE"
3. Execute "docker network create nginx_network"
4. Run "docker compose up -d"
5. Execute "docker ps -a". You have to find CONTAINER ID of your telegrambot-main-bot.
6. Execute "docker exec -it e7256b328de8 bash" where e7256b328de8 is your container id.
7. Execute "python manage.py AuthorizeSession" and enter the code 
8. Execute "docker ps -a". You have to find CONTAINER ID of your telegrambot-main-web.
9. Execute "docker exec -it e7256b328de9 bash" where e7256b328de9 is your container id.
10. Execute "python manage.py AuthorizeSession" and enter the code 
11. Execute "exit" to exit from bash