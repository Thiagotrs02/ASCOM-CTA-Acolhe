from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/triagem')
def triagem():
    return render_template('triagem.html')

@app.route('/acolhimento')
def acolhimento():
    return render_template('acolhimento.html')

if __name__ == '__main__':
    app.run(debug=True)