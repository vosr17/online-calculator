from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/division')
def div():
    value1=request.args.get('A',default = 0)
    value2=request.args.get('B',default = 0)
    result=Fraction(value1)/Fraction(value2)
    print (float(result).is_integer())
    if float(result).is_integer():
        result = int (result)
        return '%d \n' % result
    return ('%.14f' % result).rstrip('0').rstrip('.') 

if __name__ == "__main__":
    app.run()


