# app.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # This will render a webpage with control buttons

if __name__ == '__main__':
    app.run(debug=True)
