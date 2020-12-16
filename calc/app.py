# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add_vals():
    """ add a and b """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    response = add(a, b)
    return str(response)


@app.route('/sub')
def sub_vals():
    """ subtract a and b """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    response = sub(a, b)
    return str(response)


@app.route('/mult')
def mult_vals():
    """ multiply a and b """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    response = mult(a, b)
    return str(response)


@app.route('/div')
def div_vals():
    """ divide a and b """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    response = div(a, b)
    return str(response)


all_operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<operation>")
def all_math(operation):

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    response = all_operations[operation](a, b)
    return str(response)
