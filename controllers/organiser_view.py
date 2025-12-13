from flask import Blueprint,render_template,request,session,redirect,url_for,flash
from functools import wraps
from .__init__ import connect_database

o_view = Blueprint('organiser',__name__)


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id' not in session or session.get('role') != 'organiser':
            flash("You need Admin Access to access the page","danger")
            return redirect(url_for('base.home'))
        return f(*args, **kwargs)
    return decorated_function

@o_view.route('/dashboard', methods=['GET'])
@admin_required
def organiser_dashboard():
    conn = connect_database()
    cur = conn.cursor()

    cur.execute('''
                    SELECT e.id, e.title, e.description,e.date, COUNT(r.id) as registrations_count
                    FROM EVENTS e
                    LEFT JOIN REGISTRATIONS r ON e.id = r.event_id
                    WHERE e.created_by = ?
                    GROUP BY e.id
                ''',(session['id'],))
    events_created_by_organiser=cur.fetchall()

    conn.close()

    return render_template("organisers_dashboard.html",events=events_created_by_organiser)

@o_view.route('/create_event', methods=['POST'])
@admin_required
def create_event():
    if request.method == "POST":
        title = request.form['title']
        description=request.form['description']
        date=request.form['date']
        organiser=session['id']

        conn=connect_database()
        cur=conn.cursor()
        cur.execute('''
                    INSERT INTO EVENTS (title, description, date, created_by) VALUES (?,?,?,?)''',
                    (title, description, date, organiser))
        conn.commit()
        conn.close()

        flash("Event created successfully","success")
        return redirect(url_for("organiser.organiser_dashboard"))
    
'''
keys to be added in frotend
    title
    description
    date
    
'''
