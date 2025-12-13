from flask import Blueprint,render_template,request,session,redirect,url_for,flash
from .__init__ import connect_database

o_view = Blueprint('organiser',__name__)


@o_view.route('/dashboard', methods=['GET'])
def organiser_dashboard():
    conn = connect_database()
    cur = conn.cursor()

    cur.execute('''
                    SELECT e.id, e.title, e.description, COUNT(r.id) as registrations_count
                    FROM EVENTS e
                    LEFT JOIN REGISTRATIONS r ON e.id = r.event_id
                    WHERE e.organizer_id = ?
                    GROUP BY e.id VALUES (?,?,?,?)
                ''',(session['id'],))
    conn.execute()
    conn.close()

    return "Dashboard template with events list"

@o_view.route('/create_event', methods=['POST'])
def create_event():
    if request.method == "POST":
        title = request.form['title']
        description=request.form['description']
        date=request.form['date']
        organiser=session['id']

        conn=connect_database()
        cur=conn.cursor()
        cur.execute('''
                    INSERT INTO EVENTS (title, description, date, organizer_id) VALUES (?,?,?,?)''',
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
