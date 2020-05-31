from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

def take_inputs():
    v1 = request.args.get('A', default=0, type=str)
    try:
        v1 = Fraction(v1)
    except ZeroDivisionError:
        return "A's denominator should not be zero! \n"
    except ValueError:
        return "A's value should be a number (includes fraction, float, integer). \n"
    v2 = request.args.get('B', default=0, type=str)
    try:
        v2 = Fraction(v2)
    except ZeroDivisionError:
        return "B's denominator should not be zero! \n"
    except ValueError:
        return "B's value should be a number (which includes fraction, float, integer). \n"
    return v1, v2

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/mul')
def multiplication():
    try:
        v1, v2 = take_inputs()
        result = v1 * v2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return ('%.14f' % result).rstrip('0').rstrip('.')

if __name__ == "__main__":
    app.run()