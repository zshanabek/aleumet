# Aleumet

Telegram bot saves data about users and forwards it to group chat.

aleumet - word from Kazakh әлеумет ("community").

## Installation

1. Clone repository

```bash
git clone https://github.com/zshanabek/aleumet
cd aleumet
```

2. Install dependencies via `pipenv` package management system

```bash
pipenv install
```

3. Run server

```bash
python manage.py runserver
```

## Bot
1. Create the environment variables file named `.env`. In it write down config variables.

```text
number_of_users = 3
max_posts_per_user = 4
max_likes_per_user = 5
```

2. Run bot

```bash
python bot.py
```
