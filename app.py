from flask import Flask, render_template, request, redirect
from functions import get_students, get_student_by_id, insert_student, is_not_none, remove_student_by_id, update_student_by_id

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    students = get_students()
    return render_template("index.html", items=students)

@app.route('/addStudent', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Проверяю значение на None
        if is_not_none(request.form['name']):
            # Если студент успешно добавлен, тогда перенаправляем к списку
            if(insert_student(request.form['name'])):
                return redirect('/index')
            # Если произошла какая-то ошибка, показываем ошибку
            return render_template('addStudent.html', errors=["Ошибка 505"]) 
    else:
        return render_template('addStudent.html', errors=None)
    
@app.route('/removeStudent/<int:id>', methods=['GET', 'POST'])
def remove_student(id):
    if request.method == 'POST':
        id = request.form['id']
        student = get_student_by_id(id)

        if(remove_student_by_id(id)):
            return redirect('/index')

        return render_template('removeStudent.html', item=student, errors=["Ошибка 505"]) 
    else:
        student = get_student_by_id(id)
        if student == None:
            return redirect('index')
        return render_template('removeStudent.html', item=student, errors=None)

@app.route('/updateStudent/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        student = get_student_by_id(id)

        if(update_student_by_id(id, name)):
            return redirect('/index')

        return render_template('updateStudent.html', item=student, errors=["Ошибка 505"]) 
    else:
        student = get_student_by_id(id)
        if student == None:
            return redirect('index')
        return render_template('updateStudent.html', item=student, errors=None)