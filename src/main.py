from flask import Flask, render_template
from dotenv import load_dotenv
from os import getenv

load_dotenv() # Load env variables

app = Flask(__name__) # __name__ is used to resolve resources
 
@app.get("/")
def index():
    return render_template("index.html")

@app.get("/about")
def about():
    return "About me"

if __name__ == "__main__":
    debug = getenv("DEBUG") == "True" # Get debug mode from env variables

    app.run(debug=debug) # Debug mode is enabled, rerun the server when you make changes