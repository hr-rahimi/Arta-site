from flask import Flask , render_template ,url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def Home_Page():
    return render_template("home.html")

@app.route("/about")
def About_page():
    return "<h1>درباره ما </h1>"




if __name__ == "__main__":
    app.run(debug = True)