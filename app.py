from flask import Flask, render_template, request

app=Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("calculator.html")


def addNums(number1, number2):
    total = number1 + number2
    return str(total)


@app.route("/", methods=["POST"])
def add_handler():
    number1 = int(request.form["num1"])
    number2 = int(request.form["num2"])
    return addNums(number1, number2)
