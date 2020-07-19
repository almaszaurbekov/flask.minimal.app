import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-5J1MT1O\SQLEXPRESS01;DATABASE=PythonDB;')
cursor = conn.cursor()

def get_students():
    try:
        cursor.execute("SELECT * FROM Student")
        return jsonify_list(cursor.fetchall())
    except:
        return None

def get_student_by_id(id):
    try:
        cursor.execute(f"SELECT * FROM Student WHERE Id = {id}")
        return jsonify(cursor.fetchone())
    except:
        return None

def insert_student(name):
    try:
        cursor.execute(f"INSERT INTO Student(name) VALUES ('{name}')")
        conn.commit()
        return True
    except:
        return False

def remove_student_by_id(id):
    try:
        cursor.execute(f"DELETE FROM Student WHERE Id = {id}")
        conn.commit()
        return True
    except:
        return False

def update_student_by_id(id, name):
    try:
        cursor.execute(f"UPDATE Student SET Name = '{name}' WHERE Id = {id}")
        conn.commit()
        return True
    except:
        return False

def jsonify_list(rows):
    return [jsonify(row) for row in rows]

def jsonify(row):
    return {
        "id" : row[0],
        "name" : row[1]
    }

def is_not_none(value):
    return value != None and value != ""