import json
import pandas as pd
from io import StringIO
from flask import Flask, render_template, request
from pandas.errors import EmptyDataError

import file_generator

app = Flask(__name__)


@app.route("/")
def home():
    """ Display the application's home page. """
    return render_template("home.html")


@app.route("/processor", methods=["GET", "POST"])
def process_file():
    """ Process the input file and display the results. """
    if request.method == "POST":
        fso = request.files["file"]
        messages, df = read_input_to_df(fso)
        if df is not None:
            messages, content = file_generator.main(df)
            categories = json.dumps(content, sort_keys=False, indent=4, separators=(",", ": "))
        else:
            categories = "null"
    else:
        messages = ["Sorry, need to upload a file first."]
        categories = "null"
    status_code = 400 if categories == "null" else 201
    return render_template("status.html", messages=messages, response=categories), status_code


def read_input_to_df(fso):
    """ Read input file to dataframe and perform cleanup on it. """
    if not fso.filename.endswith(".csv") or fso.filename == "":
        return ["Sorry, input file must be in csv format."], None
    try:
        csv_file = StringIO(fso.stream.read().decode(encoding="utf-8"))
        df = pd.read_csv(csv_file, dtype=str)
    except EmptyDataError:
        return ["Sorry, the input file seems to be empty."], None

    # Filter out those rows which do not contain any data
    df = df.dropna(how="all")
    return None, df


if __name__ == "__main__":
    app.run(debug=False)
