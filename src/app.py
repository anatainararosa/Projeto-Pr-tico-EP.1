from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contatos')
def contatos():
    return render_template('contacts.html')

@app.route('/sobremim')
def sobremim():
    return render_template('sobremim.html')
    
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')