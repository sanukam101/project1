from flask import Flask
num1 = 1.5
num2 = 6.3
sum = num1 + num2
app = Flask(__name__)

@app.route('/')
def hello():# This program adds two numbers




# Add two numbers



    return 'The sum of {0} and {1} is {2}'.format(num1, num2, sum)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
