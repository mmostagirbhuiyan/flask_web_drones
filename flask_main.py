from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/action/')
def action():
    return render_template("action.html")


@app.route('/hubsan/')
def hubsan():
    return render_template("hubsan.html")


@app.route('/insight/')
def insight():
    return render_template("insight.html")


@app.route('/phantom/')
def phantom():
    return render_template("phantom.html")


@app.route('/syma/')
def syma():
    return render_template("syma.html")


@app.route('/udi/')
def udi():
    return render_template("udi.html")


if __name__ == "__main__":
    app.run(debug=True)
