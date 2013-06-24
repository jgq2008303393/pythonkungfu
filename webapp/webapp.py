from flask import Flask
from flask import render_template
from flask import Response

app = Flask('webapp')


def plain(text):
    return Response(
        response=text,
        status=200,
        headers=None,
        mimetype='application/x-javascript',
        content_type=None,
        direct_passthrough=False
    )


@app.route("/")
def index():
    json = {
        "greet": "Holla",
        "name": "blusp10it"
    }
    return render_template('index.html', data=json)


@app.route("/hello")
def hello():
    return plain("Hello world!")

if __name__ == "__main__":
    app.run(debug=True)
