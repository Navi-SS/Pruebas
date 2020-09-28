from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is "+ str(number+1)

@app.route('/<string:name>/')
def helloyou(name):
    return "Hello "+name

@app.route('/api/sps/helloworld/v1')
def hello():
    return jsonify({'name':'Iván','address':'México','project':'Test 1','Language':'Python'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)