from flask import Blueprint,render_template,request,session,redirect,url_for,flash
from .__init__ import connect_database

b_view = Blueprint('base',__name__)


@b_view.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['user_email']
        password = request.form['user_password']
        conn = connect_database()
        cur = conn.cursor()
        cur.execute('SELECT * FROM USERS WHERE email=?',(email,))
        user=cur.fetchone()
        conn.close()
        if user and password==user['password']:
            if user['role']!="organizer":
                session['id'] = user['id']
                session['email'] = user['email']
                session['role'] = 'user'
                return "USER DASHBOARD" # to be added
            else:
                session['id'] = user['id']
                session['email'] = user['email']
                session['role'] = "organizer"
                return "ADMIN DASHBOARD" # to be added
        else:
            flash("Incorrect Email or Password","danger")
    return render_template('index.html')

'''
keys to be added in frotend
    user_email
    user_password

'''

@b_view.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['user_name']
        email = request.form['user_email']
        password = request.form['user_password']
        confirm_password = request.form['user_confirm_password']
        role = request.form['role']
        
        conn = connect_database()
        cur = conn.cursor()

        if not(password == confirm_password):
            flash("Password do not match","danger")
            conn.close()
            return redirect(url_for('base.register'))
        
        cur.execute('SELECT id from users WHERE email = ?',(email,))
        existing_user = cur.fetchone()

        if existing_user:
            flash("Email already registered!. Login or use a different email", "danger")
            conn.close()
            return redirect(url_for('base.home'))
        
        cur.execute('INSERT INTO USERS (name,email,password,role) VALUES (?,?,?,?)',(name,email,password,role))
        conn.commit()
        conn.close()
        flash("Account Registered Succesfully","success")
        return redirect(url_for('base.home'))
    return render_template('register.html')
'''
keys to be added in frotend
    user_email
    user_name
    user_password
    user_confirm_password
    role
    
'''
