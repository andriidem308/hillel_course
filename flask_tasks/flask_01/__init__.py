from flask import Flask, render_template
from faker import Faker
from string import printable
from random import choice
import requests


app = Flask(__name__)


@app.route('/')
def main_page() -> str:
    return render_template('index.html')


@app.route('/users/generate')
@app.route('/users/generate/<int:n>')
def generate_users(n=20) -> str:
    fk = Faker()
    gen_names = [fk.name() for _ in range(n)]
    gen_emails = [fk.free_email() for _ in range(n)]
    gen_users = tuple(zip(gen_names, gen_emails))
    res = '<br>' + '<br>'.join(map(', '.join, gen_users))
    return render_template('users-gen.html') + res


@app.route('/password/generate')
@app.route('/password/generate/<int:n>')
def generate_password(n=8) -> str:
    password = ''
    for _ in range(n):
        password += choice(printable)

    res = f'<p>Random password: {password}</p>'
    return render_template('pass-gen.html') + res


@app.route('/astro')
def astro_counter() -> str:
    json_data = requests.get("http://api.open-notify.org/astros.json", json={"key": "value"}).json()
    res = "Astronauts' amount: " + str(json_data['number'])
    return render_template('astro.html') + res


if __name__ == "__main__":
    app.run()


