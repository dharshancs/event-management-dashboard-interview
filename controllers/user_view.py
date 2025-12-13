from flask import Blueprint,render_template,request,session,redirect,url_for,flash
from .__init__ import connect_database

u_view = Blueprint('user',__name__)


@u_view.route('/dashboard', methods=['GET'])
def user_dashboard():
    conn = connect_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM EVENTS")
    all_events = cur.fetchall()

    cur.execute('''
                SELECT event_id FROM REGISTRATIONS WHERE user_id=? VALUES (?)
            ''',(session['id']))
    events_user_registered = cur.fetchall()
    conn.close()
    return "user dashboard with all_events and events_user_registered"

@u_view.route('/book/<int:event_id>')
def book_event(event_id):
    conn=connect_database()
    cur = conn.cursor()
    cur.execute("INSERT INTO REGISTRATIONS(user_id,event_id) VALUES(?,?)",(session['id'],event_id))
    conn.commit()
    conn.close()
    return redirect(url_for("user.user_dashboard"))
