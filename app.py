from flask import Flask, make_response, jsonify
from dbcreds import production_mode
from dbhelpers import run_statement

app = Flask(__name__)


@app.get('api/animals')
def get_animals():
    result = run_statement("CALL get_all_animals")
    keys = ["animalName", "numberOfLegs"]
    response = []
    if (type(result) == list):
        for animal in result:
            response.append(dict(zip(keys, animal)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(result), 500)
    





if (production_mode == True):
    print("Running server in production mode")
    import bjoern #type:ignore
    bjoern.run(app, "0.0.0.0", 5000)
else:
    print("Running in testing mode")
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)