#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import request
import urllib


app = Flask('webapp')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/calculator")
def calculator():
    return render_template('calculator.html')


@app.route("/calculator", methods=["POST"])
def post():
    datas = urllib.unquote(request.data).decode('utf8').encode('ascii', 'ignore')
    segment1 = (datas.split('&')[0]).split('=')[1]
    segment2 = (datas.split('&')[1]).split('=')[1]
    segment3 = (datas.split('&')[2]).split('=')[1]
    hasil = 0
    if segment2 == "+":
        hasil = float(segment1) + float(segment3)
        hasil = str(hasil)
    if segment2 == "-":
        hasil = float(segment1) - float(segment3)
        hasil = str(hasil)
    if segment2 == "*":
        hasil = float(segment1) * float(segment3)
        hasil = str(hasil)
    if segment2 == "/":
        hasil = float(segment1) / float(segment3)
        hasil = str(hasil)
    return hasil

if __name__ == "__main__":
    app.run()
