from flask import Flask, render_template, request
import sqlite3
import os
from flask_mail import Mail, Message

app = Flask(__name__)

# Setup Mail (Doctor only)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# Replace with your actual Gmail address and app password
app.config['MAIL_USERNAME'] = 'konardhanalakshmi@gmail.com'
app.config['MAIL_PASSWORD'] = 'Dhanam@2004'  # Use your Gmail app password
mail = Mail(app)

# Database setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Use the correct path to the actual database file inside the 'data' folder
DB_PATH = os.path.join(BASE_DIR, 'data', 'appointments.db')

def init_db():
    # Ensure the data directory exists
    data_dir = os.path.join(BASE_DIR, 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    phone TEXT,
                    date TEXT,
                    time TEXT,
                    doctor TEXT
                )''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        doctor = request.form['doctor']

        # Save to DB
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO appointments (name, email, phone, date, time, doctor) VALUES (?, ?, ?, ?, ?, ?)",
                  (name, email, phone, date, time, doctor))
        conn.commit()
        conn.close()


        # Send email to doctor only
        try:
            msg = Message('New Appointment Booked',
                          sender=app.config['MAIL_USERNAME'],
                          recipients=[app.config['MAIL_USERNAME']])
            msg.body = f"""
            New Appointment Details:
            Name: {name}
            Email: {email}
            Phone: {phone}
            Date: {date}
            Time: {time}
            Doctor: {doctor}
            """
            mail.send(msg)
        except Exception as e:
            print(f"Error sending email: {e}")

        return render_template('success.html')

    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
