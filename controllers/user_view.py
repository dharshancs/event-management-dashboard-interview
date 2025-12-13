from flask import Blueprint,render_template,request,session,redirect,url_for,flash
from functools import wraps
from flask import jsonify
import sqlite3
from .__init__ import connect_database
from datetime import datetime, timedelta #we use it for notifications

u_view = Blueprint('user',__name__)

#decorator function for login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id' not in session:
            flash("You need to login to access this page","danger")
            return redirect(url_for('base.home'))
        return f(*args, **kwargs)
    return decorated_function

@u_view.route('/dashboard', methods=['GET'])
@login_required
def user_dashboard():
    conn = connect_database()
    cur = conn.cursor()
    cur.execute('''
                SELECT e.id, e.title, e.description, e.date, COUNT(r.id) as registrations_count
                FROM EVENTS e
                LEFT JOIN REGISTRATIONS r ON e.id = r.event_id
                GROUP BY e.id
                ''')
    all_events = cur.fetchall()

    cur.execute('''
                SELECT event_id FROM REGISTRATIONS WHERE user_id=?
            ''',(session['id'],))
    events_user_registered = [row['event_id'] for row in cur.fetchall()]
    notifications=[]
    today=datetime.now().date()
    upcoming=today+timedelta(days=3)
    for event in all_events:
        if event['id'] in events_user_registered:
            try:
                event_date=datetime.strptime(event['date'],'%Y-%m-%d').date()
                if today <= event_date <= upcoming:
                    time_left=(event_date-today).days
                    if time_left==0:
                        notif=f"Reminder: '{event['title']}' will happen TODAY!"
                    else:
                        notif=f"Reminder: '{event['title']}' is upcoming in {time_left} days!"
                    notifications.append(notif)
            except:
                pass        

    conn.close()
    return render_template("user_dashboard.html",events=all_events,my_regs=events_user_registered,notifications=notifications)

@u_view.route('/book/<int:event_id>')
@login_required
def book_event(event_id):
    
    conn=connect_database()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO REGISTRATIONS(user_id,event_id) VALUES(?,?)",(session['id'],event_id))
        conn.commit()
        flash("Registered successfully","success")
    except sqlite3.IntegrityError:
        flash("You are already registered for this event.", "info")        
    finally:
        conn.close()
    return redirect(url_for("user.user_dashboard"))

@u_view.route('/api/stats')
@login_required
def real_time_stats():
    conn=connect_database()
    cur = conn.cursor()
    cur.execute('''
        SELECT e.id, COUNT(r.id) as registrations_count
        FROM EVENTS e
        LEFT JOIN REGISTRATIONS r ON e.id = r.event_id
        GROUP BY e.id
    ''')
    data = cur.fetchall()
    conn.close()
    stats={row['id']: row['registrations_count'] for row in data}
    return jsonify(stats) 



