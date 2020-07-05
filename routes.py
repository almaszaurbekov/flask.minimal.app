from flask import render_template, flash, redirect
from app import app
from functions import get_vacancies, get_vacancy_by_id

@app.route('/')
@app.route('/index')
def index():
    vacancies = get_vacancies()
    return render_template('index.html', title='Index', vacancies=vacancies)

@app.route('/vacancies/<id>')
def vacancies_details(id):
    # vacancy = get_vacancy_by_id(id)
    return render_template('details.html', title='Details')