# aquila-metrics-service
Python REST API for statistical calculations

Features:

- Accepts numeric inputs from HTTP POST requests
- Calculates:
    - Mean
    - Median
    - Standard Deviation
    - Minimum
    - Maximum
- Returns results as JSON
- Error handling implemented for:
    - Missing or invalid JSON payload
    - Missing "input" key
    - Lists containing less than 2 numbers
    - Non-numeric inputs

Installation:

- Clone the repository:
```
git clone https://github.com/EC-DMU/metrics-calculator.git
```

- Enter the directory:
```
cd metrics-calculator
```

- Download dependencies:
```
pip install -r requirements.txt
```

How to run:

- Start the Flask server:
```
python api/api.py
```

- The API will listen on port 5050


Example Request:
 ```
 curl -X POST http://localhost:5050/calculator -H "content-type: application/json" -d '{"input": [10, 20, 30, 40]}'
 ```

Example Response:
 ```
 {"Max":40,"Mean":25,"Median":25.0,"Standard Deviation":12.909944487358056,"min":10}
 ```
