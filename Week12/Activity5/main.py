from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def bmi():
    result = ''

    if request.method == 'POST':
        try:
            height = float(request.form['height'])  # unit: meter
            weight = float(request.form['weight'])  # unit: kg

            bmi_value = weight / (height * height)
            result = f'Your BMI is: {bmi_value:.2f}'

        except:
            result = 'Invalid input'

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>BMI Calculator</title>
    </head>
    <body>
        <h2>BMI Calculator</h2>

        <form method="post">
            <p>
                Height (meter):
                <input type="text" name="height">
            </p>

            <p>
                Weight (kg):
                <input type="text" name="weight">
            </p>

            <button type="submit">Calculate</button>
        </form>

        <h3>{result}</h3>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True)