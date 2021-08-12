# Put your app in here.
from operations import add,sub,mult,div
from flask import Flask, request

app = Flask(__name__)

@app.route('/math/<operation>')
def handle_operation(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    operations = {
        'add': add(a,b),
        'sub': sub(a,b),
        'mult': mult(a,b),
        'div': div(a,b)
    }
    return f'{operations[operation]}'
