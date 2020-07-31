import rss # custom module. Every .py file is called a module
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    docs = rss.load_rss_feed()
    return render_template("index.html", docs = docs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)