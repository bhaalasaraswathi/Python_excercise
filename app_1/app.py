from flask import Flask, render_template

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the home page ("/")
@app.route('/')
def index():
  """Renders the index.html template file."""
  return render_template('index.html')

@app.route('/budget')
def budget():
  """Renders the budget.html template file."""
  #pass variables to the template
  budget_data = {
      "total_money": 1000000,
      "rent": 300000,
      "groceries": 50000,
      "transportation": 20000,
      "utilities": 10000,
      "entertainment": 15000
  }
  #alternatively use below line
  #return render_template('budget.html', total_money=1000000, rent=300000, groceries=50000, transportation=20000, utilities=10000, entertainment=15000)
  return render_template('budget.html', **budget_data)

@app.route('/aravind')
def aravind():
  """Renders the aravind.html template file."""
  return render_template('aravind.html')

# This part runs the app
if __name__ == '__main__':
  app.run(debug=True, port=5001)