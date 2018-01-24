from flask import Flask, request, render_template, redirect

app = Flask(__name__)

encrypted_text = ''

@app.route('/', methods=['GET', 'POST'])
def cezar_handler():
    global encrypted_text
    if request.method == 'POST':
        text = list(request.form.get('text'))
        offset = int(request.form.get('offset'))
        while offset < 0:
            offset += 26
        for i, let in enumerate(text):
            if ord(let) >= 65 and ord(let) <= 90:
                text[i] = chr((ord(let) - 65 + offset) % 26 + 65)
            if ord(let) >= 97 and ord(let) <= 122:
                text[i] = chr((ord(let) - 97 + offset) % 26 + 97)
        encrypted_text = ''.join(text)
        return redirect("/")
    return render_template('cezar.html', encrypted_text=encrypted_text)

app.run(debug=True)