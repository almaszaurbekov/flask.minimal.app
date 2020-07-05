import requests
from models import Vacancy

api = "https://api.hh.ru/"

def get_vacancies(min_count=6):
    url = api + "vacancies"
    response = requests.get(url)
    json = response.json()

    if(min_count > 20):
        min_count = 20

    vacancies = []
    
    for i in range(min_count):
        item = json['items'][i]
        vacancy = Vacancy(item['id'], item['name'], item['area'], item['salary'], 
        item['address'], item['published_at'], item['created_at'], item['url'], item['snippet'])
        vacancies.append(vacancy)

    return vacancies

def get_vacancy_by_id(id):
    url = api + "vacancies/" + str(id)
    response = requests.get(url)
    json = response.json()

    # обработать json формат #
    return None
    # ---------------------- #