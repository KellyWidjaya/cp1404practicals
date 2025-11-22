from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

def convert_celsius_to_fahrenheit(celsius):
    """Calculate fahrenheit from celsius value"""
    return (celsius * 9/5) + 32

@app.route('/f/<celsius>')
def display_fahrenheit(celsius):
    fahrenheit = convert_celsius_to_fahrenheit(float(celsius))
    return f"{celsius}°C is {fahrenheit:.2f}°F"


if __name__ == '__main__':
    app.run()
