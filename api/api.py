from flask import Flask, jsonify, request

api = Flask(__name__) # creates flask instance

@api.route("/calculator", methods=["POST"]) # defines "/calculator" endpoint for only POST requests
def api_calculator():
    payload = request.get_json(silent=True) # extracts json payload, returns none if it fails
    return jsonify(payload), 200

if __name__ == "__main__":
    api.run(port=5050) # locally runs on port 5050