#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    return f'<h1>{string}</h1>'

@app.route('/count/<int:num>')
def count(num):
    display = f''
    for n in range(num):
        display += f'{n}\n'
    return display

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
        
@app.route('/print/hello')
def hello():
    print('hello')
    return 'hello'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
