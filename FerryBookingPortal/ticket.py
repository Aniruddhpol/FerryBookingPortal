from flask import Flask, render_template, request, redirect, flash,session
from flask_mysqldb import MySQL
from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'annipol2001'
app.config['MYSQL_DB'] = 'annidb'


mysql = MySQL(app)

@app.route('/', methods=['POST','GET'])
def ticket():
 
 if request.method == 'POST':
        # Fetch form data
        name = request.form['name']
        to = request.form['to']
        date = request.form['date']
        one = request.form['one']
        two = request.form['two']
      
        
        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO ticket (name, to, date, one, two) VALUES(%s, %s, %s, %s,%s)" ,
                    (name, to, date, one,two))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Your Ticket Is Booked..."Now Add Your Details"','success')
       
        return redirect('/detail')
    # return render_template('register.html')
 
 return render_template('ticket.html')

@app.route('/book', methods=['POST','GET'])
def book():
    cur = mysql.connection.cursor()
    cur.execute("select *from user_detail ORDER BY one DESC LIMIT 1;")
    data = cur.fetchall()
    cur.close()
    return render_template('book.html',user_detail=data)

# @app.route('/update', methods= ['POST', 'GET'])
# def update():
#    if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         age = request.form['age']
#         phone = request.form['phone']
#         one = request.form['one']

#         cur = mysql.connection.cursor()
        
#         cur.execute("""
#         UPDATE user_detail SET name=%s,email=%s, phone=%s, age=%s
#         WHERE one=%s
#         """, (name, email, phone, age,one))
#         flash("Data Updated Successfully")
#         return redirect(url_for('book'))
   
@app.route('/detail', methods=['POST','GET'])
def detail():
  
  if request.method == 'POST':
        # Fetch form data
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        phone = request.form['phone']
        address = request.form['address']
        nationality = request.form['nationality']
        blood_group = request.form['blood_group']
        gender = request.form['gender']
        one = request.form['one']

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO details(name, email, age, phone,address,nationality,blood_group,gender,one) VALUES(%s, %s, %s, %s,%s, %s, %s, %s, %s)",
                    (name, email, age, phone,address,nationality ,blood_group,gender,one))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('successfully added....','success')
        return redirect('/book')
 
  return render_template('user_detail.html')

@app.route('/nav', methods=['POST','GET'])
def nav():
 
 return render_template('nav.html')

@app.route('/show', methods=['POST','GET'])
def show():
 
 return render_template('show.html')

if __name__ == "__main__":
 app.run(debug=True,port=8000)