import MySQLdb
from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "123456"


app.config["MYSQL_HOST"] = "scalableservicesassignment.cz1kzfagdqhy.ap-south-1.rds.amazonaws.com"
app.config["MYSQL_USER"] = "admin"
app.config["MYSQL_PASSWORD"] = "123Amazon"
app.config["MYSQL_DB"] = "AdminInfo"

db = MySQL(app)

@app.route('/AdminSignup', methods=['GET', 'POST'])
def AdminSignup():
    if request.method == 'POST':
        if 'email' in request.form and 'password' in request.form and 'name' in request.form:
            email = request.form['email']
            password = request.form['password']
            name = request.form['name']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO AdminInfo.adminlogin (name, email, password) VALUES (%s, %s, %s)",
                           (name, email, password))
            db.connection.commit()
            return "Admin Signup Successful !!"

    return render_template("SignUp.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
    app.run(debug=True)