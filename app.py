# from flask import Flask, render_template, json, request, session, redirect
# from flaskext.mysql import MySQL

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
# pip install flask_mysqldb
import MySQLdb.cursors as mdc
# pip install flask-MySQLdb

import re

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Bhargav@2004'
app.config['MYSQL_DATABASE_DB'] = 'appointment'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/doctor-availability')
def availability():
    return render_template('doctor-availability.html')

@app.route('/booking-schedule')
def book():
    return render_template('booking-schedule.html')

@app.route('/reschedule')
def reschedule():
    return render_template('reschedule.html')

@app.route('/view-schedule')
def view_schedule():
    return render_template('view-schedule.html')

@app.route('/patient-gateway')
def patient_gateway():
    return render_template('patient-gateway.html')

@app.route('/')
def main():
    return render_template('hospital.html')

@app.route('/booking-schedule',methods=['POST'])
def Appointment_Booking():
  msg = ''
  if request.method == 'POST' and 'firstname' in request.form and 'lastname' in request.form and 'phonenumber' in request.form and 'symptoms' in request.form and 'dob' in request.form and 'departmentcode' in request.form and 'postalcode' in request.form and 'specific_requirements' in request.form and  'occupation' in request.form:
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    phonenumber = request.form['phonenumber']
    email = request.form['email']
    dob = request.form['dob']
    departmentcode = request.form['departmentcode']
    symptoms = request.form['symptoms']
    specific_requirements = request.form['specific_requirements']
    occupation = request.form['occupation']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor = mysql.connection.cursor()
    #mdc.DictCursor
    # cursor.execute(
    #     'SELECT * FROM Appointment WHERE phonenumber = % s', (phonenumber, ))
    # account = cursor.fetchone()
    # if account:
    #     msg = 'Appointment already Taken !'
    # if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
    #     msg = 'Invalid email address !'
    # elif not re.match(r'[A-Za-z]+', firstname):
    #     msg = 'name must contain only characters!'
    # elif not re.match(r'[A-Za-z]+', lastname):
    #     msg = 'name must contain only characters!'  
#  else:
    cursor.execute("INSERT INTO appointment (firstname, lastname, phonenumber,email,dob, departmentcode, symptoms,specific_requirements, occupation) VALUES (% s, % s, % d, % s, % s, % s, % s, % s, % s)",
                    (firstname, lastname, phonenumber,email,
                    dob, departmentcode, symptoms,
                    specific_requirements, occupation))
    mysql.connection.commit()
    msg = 'You Appoinment is successfully scheduled!'
  return render_template('hospital.html',msg=msg)

# redirect(url_for('hospital'))

# @app.route('/Appointment/Reschedule', methods=['GET', 'POST'])
# def Appointment_Rescheduler():
#   msg = ''
#   if request.method == 'POST' and 'firstname' in
#   request.form and 'lastname' in request.form and
#   'phonenumber' in request.form and 'email2' in
#   request.form and 'dob' in request.form and
#   'pdt' in request.form and 'pdt2'
#   in request.form:
#     firstname = request.form['firstname']
#     lastname = request.form['lastname']
#     phonenumber = request.form['phonenumber']
#     email = request.form['email']
#     email2 = request.form['email2']
#     dob = request.form['dob']
#     pdt = request.form['pdt']
#     pdt2 = request.form['pdt2']
#     # specific_requirements = request.form['specific_requirements']
#     # occupation = request.form['occupation']

#     conn = mysql.connect()
#     cursor = conn.cursor()
#     # cursor = mysql.connection.cursor(mdc.DictCursor)
#     # cursor.execute(
#     #     'SELECT * FROM Appointment WHERE phonenumber = % s', (phonenumber, ))
#     # account = cursor.fetchone()
#     # if account:
#     #     msg = 'Appointment already Taken !'
#     if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#         msg = 'Invalid email address !'
#     elif not re.match(r'[^@]+@[^@]+\.[^@]+', email2):
#         msg = 'Invalid email address !'    
#     elif not re.match(r'[A-Za-z]+', firstname):
#         msg = 'name must contain only characters!'
#     elif not re.match(r'[A-Za-z]+', lastname):
#         msg = 'name must contain only characters!'  
#     else:
#         cursor.execute('INSERT INTO Appointment_Rescheduler VALUES \
#         (NULL, % s, % s, % s, % s, % s, % s, % s, % s, % s)',
#                         (firstname, lastname, phonenumber,email,
#                         email2, dob, pdt, pdt2,))
#         mysql.connection.commit()
#         msg = 'You Appoinment is successfully Re-scheduled! to {{pdt2}}'
#   return render_template('register.html', msg=msg)



if __name__ == "__main__":
    app.run(debug=True)
