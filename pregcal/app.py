from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_due_date', methods=['POST'])
def calculate_due_date():
    last_period = request.form['last_period']
    
    try:
        last_period_date = datetime.strptime(last_period, '%Y-%m-%d')
    except ValueError:
        return render_template('index.html', error="Invalid date format. Please use YYYY-MM-DD.")

    due_date = last_period_date + timedelta(days=280)  # Assuming a standard 280-day pregnancy

    return render_template('index.html', due_date=due_date.strftime('%Y-%m-%d'))

if __name__ == '__main__':
    app.run(debug=True)
