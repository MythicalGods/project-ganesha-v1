from flask import Flask, render_template
from dotenv import load_dotenv
from os import getenv
from repositories.post_repository import PostRepository

load_dotenv() # Load env variables

app = Flask(__name__) # __name__ is used to resolve resources
posts = PostRepository().get_all() # Get all posts
 
@app.get("/")
def index():
    return render_template("index.html", posts=posts)

@app.get("/about")
def about():
    return render_template("about.html") 

if __name__ == "__main__":
    debug = getenv("DEBUG") == "True" # Get debug mode from env variables

    app.run(debug=debug) # Debug mode is enabled, rerun the server when you make changes