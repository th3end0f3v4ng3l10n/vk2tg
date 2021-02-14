# vk2tg
message forwarder :)


Программа пересылает сообщения из VK в Телеграмм

<h1> pre-install </h1>


Отредактируйте ссылку:

https://api.vk.com/oauth­/token?grant_type=password​&client_id=2274003​&client_secret=hHbZxrka2uZ6jB1inYsH​&username=НОМЕР-ТЕЛЕФОНА​&password=МОЙ-ПАРОЛЬ

И перейдите по ней.
Полученный токен запишите в config.ini <h3>под Vk</h3>, где указан 'token='.
Запишите ваш номер телефона и пароль в config.ini <h3>под Vk</h3>, где указаны "login=", "password=" соответственно

Создайте бота в телеграм с помощью BotFather, скопируйте его token и вставьте <h3> Под Telegram </h3>

На этом самая сложная часть кончилась :)

<h1> Установка </h1>

<h2>LINUX:</h2>
    pip3 install -r requirements.txt

<h2>WINDOWS:</h2>
    pip intall -r requirements.txt
    
<h1> Запуск <h1>
    python3 run.py



Author: @th3end0f3v4ng3l10n
