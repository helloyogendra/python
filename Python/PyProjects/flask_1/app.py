from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1> Hello Flask</h1>"

@app.route('/info')
def info():
    return helper('Tom')

@app.route("/dynamic_page/<name>")
def dynamic_page_function(name: str):
    return f"<h1> Page for {name.capitalize()}</h1></br><h3> Good {name} </h3>"


@app.route("/html")
def get_html():
    return render_template('app.html')


@app.route("/variable")
def get_variable():
    import random
    number = random.randint(1000, 9000)
    letters = ['mango', "cherry", "banana"]
    return render_template('variable.html', value = number, fruits=letters)


def helper(name):
    return f"<p><h2><b>Hey {name} </b></h2></p>"


if __name__ == '__main__':
    app.run()                   #app.run(debug=True)