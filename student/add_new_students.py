import datetime
import sqlite3
import xlrd

all_students = xlrd.open_workbook('Students.xls')  #deschidem fisierul excel Students.xls
sheet = all_students.sheet_by_name("Sheet1")       #accesam sheetul unde sunt studentii

database = sqlite3.connect('../db.sqlite3')     #ne conectam la baza de date

cursor = database.cursor()  #definim un cursor si il folosim pentru a traversa in baza de date linie cu linie

for row in range(1, sheet.nrows):
    first_name = str(sheet.cell(row, 0).value)
    last_name = str(sheet.cell(row, 1).value)
    age = int(sheet.cell(row, 2).value)
    cnp = int(sheet.cell(row, 3).value)
    date_of_birth = '2021-01-01'
    email = str(sheet.cell(row, 5).value)
    active = 1
    created_at = datetime.datetime.now()
    update_at = datetime.datetime.now()
    values = (first_name, last_name, age, cnp, date_of_birth, email)
    query = F"INSERT INTO student_student(first_name, last_name, age, cnp, date_of_birth, email, active, created_at, updated_at)" \
            F" VALUES ('{first_name}', '{last_name}', '{age}', '{cnp}', '{date_of_birth}', '{email}', '{active}', '{created_at}', '{update_at}');"
    cursor.execute(query)

cursor.close()
database.commit()
database.close()