from flask import Flask, jsonify, request
import statistics

api = Flask(__name__) # creates flask instance

@api.route("/calculator", methods=["POST"]) # defines "/calculator" endpoint for only POST requests
def api_calculator():
    # payload = request.get_json(silent=True) # extracts json payload, returns none if it fails
    data = [19, 24, 55, 31, 16]

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