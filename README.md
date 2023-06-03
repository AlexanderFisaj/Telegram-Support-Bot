<p align="center"><a href="https://github.com/fabston/Telegram-Support-Bot" target="_blank"><img src="https://raw.githubusercontent.com/fabston/Telegram-Support-Bot/master/assets/logo.png"></a></p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-380/"><img src="https://img.shields.io/badge/python-3.9-blue.svg?style=plastic" alt="Python version"></a>
    <a href="https://github.com/fabston/Telegram-Support-Bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/fabston/Telegram-Support-Bot?style=plastic" alt="GitHub license"></a>
    <a href="https://github.com/fabston/Telegram-Support-Bot/issues"><img src="https://img.shields.io/github/issues/fabston/Telegram-Support-Bot?style=plastic" alt="GitHub issues"></a>
    <a href="https://github.com/fabston/Telegram-Support-Bot/pulls"><img src="https://img.shields.io/github/issues-pr/fabston/Telegram-Support-Bot?style=plastic" alt="GitHub pull requests"></a>
    <br /><a href="https://github.com/fabston/Telegram-Support-Bot/stargazers"><img src="https://img.shields.io/github/stars/fabston/Telegram-Support-Bot?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/fabston/Telegram-Support-Bot/network/members"><img src="https://img.shields.io/github/forks/fabston/Telegram-Support-Bot?style=social" alt="GitHub forks"></a>
    <a href="https://github.com/fabston/Telegram-Support-Bot/watchers"><img src="https://img.shields.io/github/watchers/fabston/Telegram-Support-Bot?style=social" alt="GitHub watchers"></a>
</p>

<p align="center">
  <a href="#about">About</a>
  •
  <a href="#features">Features</a>
  •
  <a href="#installation">Installation</a>
  •
  <a href="#images">Images</a>
  •
  <a href="#how-can-i-help">Help</a>
</p>

## О Телеграмм боте техподдержки
**Telegram Support Bot** 📬 помогает вам управлять запросами в службу поддержки и организовывать их.

## Особенности
- поддерживается пересылка **Text**, **Photos**, **Documents** и **Stickers**
- защита от СПАМа (чувствительность может быть установлена в конфигурационном файле [`config.py`](https://github.com/fabston/Telegram-Support-Bot/blob/master/config.py))
- фильтр нецензурных/плохих слов (с использованием регулярных выражений, слова могут быть заданы в конфигурационном файле [`config.py`](https://github.com/fabston/Telegram-Support-Bot/blob/master/config.py))
- Список всех открытых/неотвеченных заявок (также отображается время, прошедшее с момента открытия заявки)
- Запрещать / разбанивать пользователей (через ответ или user ID). Пользователь больше не сможет взаимодействовать с ботом
- Список запрещенных пользователей с указанием последней точки взаимодействия
- Настраиваемый текст FAQ
- Определите язык пользователя и отобразите его в виде эмодзи

> 💡 Есть идея для новой функции? Открыть [issue](https://github.com/fabston/Telegram-Support-Bot/issues/new?assignees=&labels=enhancement&template=feature-request---.md) и я мог бы это реализовать.

### Шаблоны комманд
| Command | Description |
| --- | --- |
| /ban | Заблокировать пользователя по ID или ответиту |
| /unban | Разблокировать пользователя по ID или ответиту |
| /banned | Список заблокированных пользователей |
| /tickets or /t | Список открытых заявок |
| /close or /c | Вручную закройте заявку с помощью ответа |

### User commands
| Command | Description |
| --- | --- |
| /start | Запустить бота |
| /faq | Показать FAQ |


## Installation
> ⚠️ Лучше всего запускать бота на VPS. Я могу порекомендовать <a href="https://hetzner.cloud/?ref=tQ1NdT8zbfNY" title="Get €20 in cloud credits">Hetzner</a>'s CX11 VPS for 2.89€/месяц. [Sign up](https://hetzner.cloud/?ref=tQ1NdT8zbfNY) прямо сейчас и получите **€20 бесплатных** кредитов.
1. Войдите в MySQL (`sudo mysql`) и создайте выделенную базу данных и пользователя с помощью следующих команд:
   1. `CREATE DATABASE TelegramSupportBot;`
   1. `CREATE USER 'SupportBotUser'@'localhost' IDENTIFIED BY '<YOUR PASSWORD>';`
   1. `GRANT ALL PRIVILEGES ON TelegramSupportBot . * TO 'SupportBotUser'@'localhost';`
   1. `exit;`
1. Клонировать этот репозиторий `git clone https://github.com/fabston/Telegram-Support-Bot.git`
1. Создайте свою виртуальную среду `python3 -m venv Telegram-Support-Bot`
1. Активируйте его `source Telegram-Support-Bot/bin/activate && cd Telegram-Support-Bot`
1. Установите все требования `pip install -r requirements.txt`
1. Редактировать и обновлять [`config.py`](https://github.com/fabston/Telegram-Support-Bot/blob/master/config.py)
1. Запустите бота `python main.py`


## Изображения
![Telegram Support Bot](https://raw.githubusercontent.com/fabston/Telegram-Support-Bot/master/assets/about.jpg)

## Как я могу помочь?
Приветствуются все виды пожертвований 🙌! Самый простой способ продемонстрировать свою поддержку - это `⭐️ star` проект, или привлеч [`🐞 issues`](https://github.com/fabston/Telegram-Support-Bot/issues/new/choose). 

***

<p align="center">
    <a href="https://www.buymeacoffee.com/fabston"><img alt="Buy Me A Coffee" title="☕️" src="https://github.com/fabston/Telegram-Airdrop-Bot/blob/main/assets/bmac.png?raw=true" width=200px></a>
</p>