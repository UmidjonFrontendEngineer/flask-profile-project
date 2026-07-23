from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='assets')

user_db = {}

valyutalar = {
    'USD': 12600,
    'EUR': 14364,
    'RUB': 163.8,
    'GBP': 16884,
    'CHF': 14490,
    'CAD': 9198,
    'KWD': 40698,
    'BHD': 33390,
    'OMR': 32760,
    'JOD': 17766,
}

komissiya = 2


def handleValyuta(summ, valyuta):
    return f"result: {summ * valyutalar[valyuta] / 100 * (100 - komissiya)} SO'M, komissiya: {komissiya}%"

@app.route('/')
def index():
    return render_template('register.html', valyutalar=valyutalar)


@app.route('/register', methods=['POST'])
def register():
    # user_db['name'] = request.form.get('name')
    # user_db['age'] = request.form.get('age')
    # user_db['email'] = request.form.get('email')

    selectValyuta = request.form.get('valyuta')
    summ = int(request.form.get('summ'))

    user_db['result'] = handleValyuta(summ, selectValyuta)

    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return render_template('profile.html', user=user_db)


if __name__ == '__main__':
    app.run(debug=True)