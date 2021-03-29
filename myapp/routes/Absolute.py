import math
from fractions import Fraction
from flask import request, jsonify
from myapp import app



@app.route('/absolute/<int:a>', methods=['POST'])
def absolute(a):
    return(f"the absolute value of {a} is {math.fabs(a)}")


if __name__ == '__main__':
    print(absolute(int(input("Please input the number: "))))