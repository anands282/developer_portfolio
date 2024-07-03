import requests
import re
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html', title='Anand Satheesh - home')


@app.route('/home')
def home():
    return render_template('base.html', title='Base')


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    contact_info_included = None

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        reason = request.form.get('reason', '').strip()

    return render_template('contact.html', title='Contact Page', contact_status=contact_info_included)


@app.route('/projects')
def projects_page():
    return render_template()


if __name__ == "__main__":
    app.run(debug=True)