from distutils.log import debug
from flask import Flask,render_template

app=Flask(__name__, template_folder='app/templates', static_folder='app/static')


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True)
