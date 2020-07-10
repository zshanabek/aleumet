import requests
from faker import Faker
from dotenv import load_dotenv
import json
import time
import os
from random import seed
from random import randint
fake = Faker()

BASE_URL = "http://localhost:8000/api"
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

USERS_NUMBER = int(os.getenv("number_of_users"))
POSTS_PER_USER = int(os.getenv("max_posts_per_user"))
LIKES_PER_USER = int(os.getenv("max_likes_per_user"))
tokens = []


def create_user(email):
    body = {
        "first_name": fake.name().split(' ')[0],
        "last_name": fake.name().split(' ')[1],
        "email": email,
        "password": "132312qQ",
        "re_password": "132312qQ"
    }
    requests.post(f'{BASE_URL}/users/', json=body)


def get_token(email):
    body = {
        'email': email,
        'password': '132312qQ'
    }
    response = requests.post(f'{BASE_URL}/token/login', json=body)
    token = json.loads(response.content)['auth_token']
    return token


def create_post(headers):
    body = {
        "title": fake.sentence(),
        "body": fake.text()
    }
    requests.post(f'{BASE_URL}/posts/', json=body, headers=headers)


def create_users():
    for _ in range(0, USERS_NUMBER):
        email = fake.email()
        create_user(email)
        tokens.append(get_token(email))


def create_posts():
    for token in tokens:
        headers = {'Authorization': f'Token {token}'}
        for i in range(0, POSTS_PER_USER):
            create_post(headers)


def like_posts(numbers):
    seed(1)
    for token in tokens:
        headers = {'Authorization': f'Token {token}'}
        for _ in range(0, LIKES_PER_USER):
            value = randint(numbers[0], numbers[-1])
            response = requests.post(
                f'{BASE_URL}/posts/{value}/like/', headers=headers)


create_users()
create_posts()

headers = {'Authorization': f'Token {tokens[0]}'}
response = requests.get(f'{BASE_URL}/posts/numbers', headers=headers)
numbers = json.loads(response.content)
like_posts(numbers)
