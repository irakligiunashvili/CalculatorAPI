import math
from fractions import Fraction
from flask import Flask


@app.route('/to_radians/<int:a>')
def absolute(a):
    return(f"the absolute value of {a} is {math.fabs(a)}")


if __name__ == '__main__':
    print(absolute(float(input("Please input the number: "))))