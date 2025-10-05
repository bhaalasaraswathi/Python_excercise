from flask import Flask, render_template

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the home page ("/")
@app.route('/')
def index():
  """Renders the index.html template file."""
  return render_template('index.html')

@app.route('/pricing')
def pricing():
  """Renders the pricing.html template file."""
  return render_template('pricing.html')

# This part runs the app
if __name__ == '__main__':
  app.run(debug=True, port=5000)