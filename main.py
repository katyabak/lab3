from flask import Flask, render_template, request
import math
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/', methods=['POST', 'GET'])
def discriminant():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    D = b**2 - 4*a*c
    if D > 0 or D == 0:
        first_x = (-b + math.sqrt(D)) / (2 * a)
        second_x = (-b - math.sqrt(D)) / (2 * a)
    else:
        first_x = complex(-b / (2 * a), math.sqrt(abs(D)) / (2 * a))
        second_x = complex(-b / (2 * a), -math.sqrt(abs(D)) / (2 * a))
    return render_template('index.html', x1 = first_x, x2 = second_x, D=D)
if __name__ == "__main__":
    app.run()