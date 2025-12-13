from flask import Blueprint,render_template,request,session,redirect,url_for,flash
from .__init__ import connect_database

u_view = Blueprint('base',__name__)


@u_view.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['user_email']
        password = request.form['user_password']
        conn = connect_database()
        curr = conn.cursor()
        curr.execute('SELECT * FROM USERS WHERE email=?',(email,))
        user=curr.fetchone()
        conn.close()
        if user and password==user['password']:
            if not user['is_admin']:
                session['id'] = user['id']
                session['email'] = user['email']
                session['is_admin'] = False
                return "USER DASHBOARD" # to be added
            elif user['is_admin']:
                session['id'] = user['id']
                session['email'] = user['email']
                session['is_admin'] = True
                return "ADMIN DASHBOARD" # to be added
        else:
            flash("Incorrect Email or Password","danger")
    return render_template('index.html')


@u_view.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['user_name']
        email = request.form['user_email']
        password = request.form['user_password']
        confirm_password = request.form['user_confirm_password']
        
        conn = connect_database()
        curr = conn.cursor()

        if not(password == confirm_password):
            flash("Password do not match","danger")
            conn.close()
            return redirect(url_for('base.register'))
        
        curr.execute('SELECT id from users WHERE email = ?',(email,))
        existing_user = curr.fetchone()

        if existing_user:
            flash("Email already registered!. Login or use a different email", "danger")
            conn.close()
            return redirect(url_for('base.home'))
        
        curr.execute('INSERT INTO USERS (name,email,password) VALUES (?,?,?)',(name,email,password))
        conn.commit()
        conn.close()
        flash("Account Registered Succesfully","success")
        return redirect(url_for('base.home'))
    return render_template('register.html')
