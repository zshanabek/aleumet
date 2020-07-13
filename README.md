# Aleumet

Simple django app with post creation by users.

aleumet - word from Kazakh әлеумет ("community").

Demo [app](https://aleumet.herokuapp.com/).

Documentation is [here](https://floating-forest-54496.herokuapp.com)

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
