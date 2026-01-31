from flask import Flask, jsonify, request # Flask Used For Building API
import statistics # for calculations

api = Flask(__name__) # creates flask instance

@api.route("/calculator", methods=["POST"]) # defines "/calculator" endpoint for only POST requests
def api_calculator():
    payload = request.get_json(silent=True) # extracts json payload, returns none if it fails
    if not payload: # checks if json payload is invalid or missing
        return jsonify({"ERROR": "Invalid Payload"}), 400
    if "input" not in payload: # checks the payload contains the "input" key
        return jsonify({"ERROR": "Missing 'input' Key In Payload"}), 400
    data = payload["input"] # extracts list from the "input" key
    if len(data) <2: # checks if there are less than two numbers in the input list
        return jsonify({"ERROR": "Must Contain At Least Two Numbers"}), 400
    if not all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in data): # checks the input list contains only numeric inputs
        return jsonify({"ERROR": "Input List Must Contain Only Numbers"}), 400

    calculations = { # stores results from the calculations below
        "Mean": statistics.mean(data),
        "Median": statistics.median(data),
        "Standard Deviation": statistics.stdev(data),
        "min": min(data),
        "Max": max(data)
    }
    return jsonify(calculations), 200

if __name__ == "__main__":
    api.run(port=5050) # locally runs on port 5050
