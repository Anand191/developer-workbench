import json
import flask
from flask import Flask, jsonify
from flask_cors import CORS
from src import SampleModel


app = Flask("QueryAutocompletion", static_url_path="", static_folder="./")
CORS(app)


@app.route("/predict", methods=['POST'])
def autocomplete():
    """
    Parameters
    ----------
    payload:
                {
                    "query": "<Query string>",
                    "metadata": {}
                }

    Returns
    -------
    list:
        [{"autocompletions": <list of autocomplete options>}]

    """
    query = flask.request.json["query"]
    model = SampleModel(num_suggestions=5)

    autocompletions = model.predict(query)
    # serialize and return
    return jsonify([{"autocompletions": json.dumps(autocompletions)}])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
