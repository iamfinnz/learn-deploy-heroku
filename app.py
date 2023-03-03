from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def main():
    return 'Ini tes aja'
    
@app.route("/hello")
def index():
    return render_template("tes.html")