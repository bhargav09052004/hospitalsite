from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ash789#p'
app.config['MYSQL_DATABASE_DB'] = 'healthcare'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

patient_counter=0
appoint_counter=0
reschedule_counter=0

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

@app.route('/hospital')
def main():
    return render_template('hospital.html')

@app.route('/sign-up')
def signup():
    return render_template('sign-up.html')

@app.route('/sign-in')
def signin():
    return render_template('sign-in.html')

@app.route('/')
def intro():
    return render_template('start.html')

@app.route('/sign-up',methods=['POST'])
def signUp():
   msg=''
   global patient_counter
   if request.method == 'POST':
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    phonenumber = request.form['phonenumber']
    email = request.form['email']
    dob = request.form['dob']
    password = request.form['password']
    current_password=request.form['current_password']
    
    conn = mysql.connect()
    cursor = conn.cursor()
    if(current_password==password):
        patient_counter=patient_counter+1
        patient_id="PH"+lastname[0]+firstname[0]+str(patient_counter)
        cursor.execute("INSERT INTO signup (patient_id,firstname, lastname,email, phonenumber,dob,password) VALUES (% s, % s, % s, % s, % s, %s, %s)",
                    (patient_id,firstname, lastname,email, phonenumber,dob,password,))
        conn.commit()
        msg='You have successfully registered your self!'
        return render_template('hospital.html',msg=msg)
    else:
        msg='Enter correct password values!!!'
        return render_template('sign-up.html',msg=msg)
    
@app.route('/booking-schedule',methods=['POST'])
def appoint():
   msg=''
#    print(request.form.keys)
#    print(request.form.values)
   global appoint_counter
   if request.method == 'POST':
    patient_id = request.form['patient_id']
    # lastname = request.form['lastname']
    # phonenumber = request.form['phonenumber']
    department = request.form['department']
    doctorname= request.form['availabledoctor']
    symptom = request.form['symptom']
    category = request.form['category']
    date = request.form['date']
    time = request.form['time']
    
    conn = mysql.connect()
    cursor = conn.cursor()
    
    cursor.execute("Select patient_id from signup where patient_id=%s",(patient_id,))
    a=cursor.fetchone()[0]
    if a:
        appoint_counter=appoint_counter+1
        appointment_id="AH"+a[0]+str(appoint_counter)
        cursor.execute("INSERT INTO appointment (patient_id,appointment_id, category,date,time,department, symptom,doctorname) VALUES (% s, % s, % s, % s, % s, %s, %s, %s)",
                    (patient_id,appointment_id, category,date,time,department, symptom,doctorname,))
        conn.commit()
        msg='You Appointment is scheduled successfully at '+date+' '+time+' '+doctorname
        return render_template('patient-gateway.html',msg=msg)
    else:
        msg='Invalid Appointment Id!!!'
        return render_template('booking-schedule.html',msg=msg)
    return render_template('booking-schedule.html')    
    
@app.route('/reschedule',methods=['POST'])
def rescheduler():
   msg=''
#    print(request.form.keys)
#    print(request.form.values)
   global reschedule_counter
   if request.method == 'POST':
    appointment_id = request.form['appointment_id']
    # lastname = request.form['lastname']
    # phonenumber = request.form['phonenumber']
    changevalue = request.form['changevalue']
    date = request.form['cad']
    time = request.form['cat']
    # print(changevalue)
    # return render_template('reschedule.html',msg=msg) 
    conn = mysql.connect()
    cursor = conn.cursor()
    if(changevalue=='no'):
        cursor.execute("Select patient_id,category,department,symptom,doctorname from appointment where appointment_id=%s",(appointment_id,))
        a=cursor.fetchone()
        if a:
            reschedule_counter=reschedule_counter+1
            appoint_id="RH"+a[0][0]+str(reschedule_counter)
            cursor.execute("Delete from appointment where appointment_id=%s",(appointment_id,))
            conn.commit()
            cursor.execute("INSERT INTO appointment (patient_id,appointment_id, category,date,time,department, symptom,doctorname) VALUES (% s, % s, % s, % s, % s, %s, %s, %s)",
                        (a[0],appoint_id, a[1],date,time,a[2], a[3],a[4],))
            conn.commit()
            msg='You Appointment is successfully re-scheduled to '+date+' '+time+' '+a[4]
            return render_template('patient-gateway.html',msg=msg)
        else:
            msg='Invalid Appointment Id!!!'
            return render_template('reschedule.html',msg=msg)
    else:
        cursor.execute("Select patient_id,category,department,symptom from appointment where appointment_id=%s",(appointment_id,))
        a=cursor.fetchone()
        if a:
            changedoctor= request.form['changedoctor']
            reschedule_counter=reschedule_counter+1
            appoint_id="AH"+a[0][0]+str(reschedule_counter)
            cursor.execute("Delete from appointment where appointment_id=%s",(appointment_id,))
            conn.commit()
            cursor.execute("INSERT INTO appointment (patient_id,appointment_id, category,date,time,department, symptom,doctorname) VALUES (% s, % s, % s, % s, % s, %s, %s, %s)",
                        (a[0],appoint_id, a[1],date,time,a[2], a[3],changedoctor,))
            conn.commit()
            msg='You Appointment is successfully re-scheduled to '+date+' '+time+' '+changedoctor
            return render_template('patient-gateway.html',msg=msg)
        else:
            msg='Invalid Appointment Id!!!'
            return render_template('reschedule.html',msg=msg)  
    
    
if __name__ == "__main__":
    app.run(debug=True)
