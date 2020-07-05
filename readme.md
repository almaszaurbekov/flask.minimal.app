# A Minimal Flask Web Application - Tutorial

[Quickstart - Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-applicatio)

Перед началом нужно выполнить команду 
```sh
$ pip install -r requirements.txt
```

Для запуска приложения вы можете использовать команду `flask` или ключ `python -m` с Flask. Прежде чем вы сможете это сделать, вы должны сообщить своему терминалу о работе приложения, экспортировав переменную среды FLASK_APP:

```sh
$ export FLASK_APP=app.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

Если вы работаете на **Windows**, синтаксис переменной среды зависит от интерпретатора командной строки. В командной строке:

```cmd
PS C:\path\to\app> $env:FLASK_APP = "app.py"
```

В качестве альтернативы вы можете использовать `python -m flask`:

```sh
$ export FLASK_APP=app.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
```

# REST API - HeadHunter

Подробнее в файлах `functions.py` и `models.py`

`get_vacancies(min_count)` - получить список свободных вакансий.

`get_vacancy(id)` - получить запись о вакансии по идентификатору.