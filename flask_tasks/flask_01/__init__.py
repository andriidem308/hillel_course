from flask import Flask
from faker import Faker
from string import printable
from random import choice
import requests


app = Flask(__name__)


@app.route('/')
def main_page() -> str:
    res = "<h1><a href='/'>Main Page</a></h1>"
    res += "<a href='/users/generate'>Generate users</a><br>"
    res += "<a href='/password/generate'>Generate passwords</a><br>"
    res += "<a href='/astro'>Astronauts' amount at the moment</a><br>"
    return res


@app.route('/users/generate')
@app.route('/users/generate/<int:n>')
def generate_users(n=20) -> str:
    res = "<h1><a href='/'>Main Page</a></h1>"
    gen_names = [Faker().name() for _ in range(n)]
    gen_emails = [Faker().free_email() for _ in range(n)]
    res += '<br>'.join(map(', '.join, tuple(zip(gen_names, gen_emails))))
    return res


@app.route('/password/generate')
@app.route('/password/generate/<int:n>')
def generate_password(n=8) -> str:
    res = "<h1><a href='/'>Main Page</a></h1>"
    password = ''
    for _ in range(n):
        password += choice(printable)

    res += 'Random password: ' + password
    return res


@app.route('/astro')
def astro_counter() -> str:
    res = "<h1><a href='/'>Main Page</a></h1>"
    json_data = requests.get("http://api.open-notify.org/astros.json", json={"key": "value"}).json()
    res += "Astronauts' amount: " + str(json_data['number'])
    return res


if __name__ == "__main__":
    app.run()


