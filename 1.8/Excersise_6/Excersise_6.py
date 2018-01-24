from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/form", methods=['GET','POST'])
def add():
    liczba1 = request.form.get('input1')
    liczba2 = request.form.get('input2')
    is_valid = False
    try:
        liczba1 = int(liczba1)
        liczba2 = int(liczba2)
        is_valid = True
    except:
        is_valid = False
    return render_template(
        'index.html',
        liczba1 = liczba1,
        liczba2 = liczba2,
        is_valid = is_valid
    )

app.run(debug=True)
