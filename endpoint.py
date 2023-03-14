from flask import Flask, request
import pickle
import json
import numpy as np

app = Flask(__name__)

# Load the saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define home route
@app.route("/")
def home():
    return "HELLO"

# Define the endpoint
@app.route('/endpoint', methods=['POST'])
def endpoint():
   if request.method == 'POST':
      # Get the JSON data from the request
      data = request.get_json()

      # Preprocess the data (e.g. scale, one-hot encode, etc.)
      input_arr = [[int(0),int(0),int(data['year']),int(data['month'])]]
      input_arr = np.array(input_arr) 

      # loading the model using pickle
      with open('model.pkl', 'rb') as f:
            model = pickle.load(f)

      # Make a prediction using the ML model
      predictions = model.predict(input_arr)

      # Convert the predictions to a JSON object
      response = json.dumps({'prediction': int(predictions[0].tolist())})

      # Set the response headers
      headers = {'Content-Type': 'application/json'}

      # Return the response
      return (response, 200, headers)


if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=False, host='0.0.0.0')
