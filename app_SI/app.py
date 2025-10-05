from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    principal = float(request.args.get('principal', 0))
    years = float(request.args.get('years', 0))
    category = request.args.get('category')

    rate = 0
    if category == 'home_loan':
        rate = 7.5
    elif category == 'car_loan':
        rate = 9.5
    elif category == 'personal_loan':
        rate = 12.5

    interest = (principal * rate * years) / 100
    print (f"Calculated Interest: {interest}")
    return render_template('index.html', si=interest)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

