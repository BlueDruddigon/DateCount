from flask import Flask, render_template, redirect, request
from datetime import datetime, date

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Flask Tutorial')

@app.route('/about')
def about():
    return render_template('about.html', title='About Page')

@app.route('/DatingCounter/<string:dates>')
def countdate(dates):
    localdate = date.today()
    inpdate = datetime.strptime(dates, '%d-%m-%Y').date()
    diff = int((localdate - inpdate).total_seconds() / (3600 * 24))
    print(diff)
    return render_template('datecount.html', title='Date Count', date=dates, value=diff)

@app.route('/date/<string:date>')
def Date(date):
    return redirect('/DatingCounter/%s' % date)

@app.route('/inputDate', methods=['GET', 'POST'])
def inpDate():
    if request.method == 'POST':
        date = request.form['date']
        return redirect('/date/%s' % date)
    return render_template('dateInput.html')

if __name__ == '__main__':
    app.run(debug=True)