# Telegram-Echo-Bot
## Introduction
I wanted to know more about telegram bots so I decided to make one! It was challenging but after alot of net surfing I was able to implement a basic telegram echo bot.
According to Telegram "Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them messages, commands and inline requests. You control your bots using HTTPS requests to our Bot API."
## Getting Started
* Open telegram desktop
* Search for "botfather"
  - BotFather is the one bot to rule them all. Use it to create new bot accounts and manage your existing bots.
  - Type /start and it will get you started!
* You will be asked to give a name to your bot.
* Also, you will be given a token to access the HTTP API which is essential to make your bot work.
* Now all you need to do is create a project folder and inside it create a virtual environment using:
  ```python 
  
  python -m venv myvenv
  ```
* Activate it using 
  ```
  myvenv\Scrips\activate
  ```
## Inside bot.py
I decided to build an echo bot cause it seemed to be the easiest thing to make. 
Mostly I followed the official telegram-bot docs:https://python-telegram-bot.readthedocs.io/en/stable/index.html 
