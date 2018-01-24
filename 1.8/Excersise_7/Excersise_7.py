from flask import Flask, render_template, request
app = Flask(__name__)
bands = [
    '3moonboys',
    'Agressiva 69',
    'Alters',
    'Appleseed',
    'Babu Król',
    'Behavior',
    'Berkut',
    'BiFF',
    'Braty z Rakemna',
    'Buldog',
    'Burdock',
    'California Stories Uncovered',
    'The Car Is on Fire',
    'Clock Machine',
    'CO.IN.',
    'Coma',
    'Cool Kids of Death',
    'Crab Invasion',
    'Curly Heads',
    'Daimonion',
    'Deriglasoff',
    'El Dupa',
    'EM',
    'George Dorn Screams',
    'Happy Pills',
]
@app.route("/")
def index():
    return render_template('index.html',
                           bands = bands)

@app.route("/search", methods=['GET'])
def add():
    query = request.args.get('query')
    if query:
        filtered_bands = [elem for elem in bands if query.lower() in elem.lower()]
    else:
        filtered_bands = bands
    return render_template('index.html',
                           bands = filtered_bands)
app.run(debug=True)