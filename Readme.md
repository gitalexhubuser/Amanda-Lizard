# AMANDA LIZARD
[![img1](https://i.imgur.com/iEhVQbu.png)](https://t.me/c/1670463029/22981)
__TASK 1:__ Бот пишет __"человек слаб"__ в случайное время, каждый день!
[![img2](https://i.imgur.com/XGysCKv.png)](https://t.me/c/1670463029/22970)
__TASK 2:__ Бот отлавливает все сообщения в [этом чате](https://t.me/+KX4rjiQrjpc2NjIy) со словом [Миша](https://regex101.com/) и пишет в ответ отправителю: __"Но я не Миша!"__

# TASK 1
## Узнать chat id __"открытого канала"__
- [Сайт](https://lavrynenko.com/get_id_from_telegram.php)
- https://api.telegram.org/bot TOKEN /getChat?chat_id=@twitch_clipz

## Узнать chat id __"закрытого канала"__
- скопировать https://t.me/c/1670463029/1
- прибавить __-100__ в начало к 1670463029
- получим: -1001670463029

## Чат ID
| Chat ID | Канал |
| ------ | ------ |
| -1001670463029 | Зазеркалье |
| -1001744761688 | Тестовый |

## CMD
Виртуальные переменные среды [гайд](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html)
```sh
set TELEGRAM_BOT_TOKEN="123"
echo %TELEGRAM_BOT_TOKEN%
```
> __Важно__: без `пробелов` после символа равно!

Перейти в папку с проектом:
```sh
cd /D "E:\YandexDisk\Python\[2023] Amanda Lizard\"# Amanda-Lizard
```

# TASK 2
Требуемые либки:
```sh
pip install python-telegram-bot --upgrade
```

