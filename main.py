import rss # custom module. Every .py file is called a module
from flask import Flask, render_template


from  time import time
import logging
from logging.config import fileConfig

app = Flask(__name__)

fileConfig('logging.ini')
logger = logging.getLogger()



@app.route('/')
def hello_world():
    start_time = time()
    docs = rss.load_rss_feed()
    duration = time() - start_time
    logger.info(f"Time taken to serve the request: {duration: .2f} seconds")
    return render_template("index.html", docs = docs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)