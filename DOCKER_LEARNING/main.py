import time 
from flask import Flask
start = time.time()
app = Flask(__name__)
def elapsed():
    running = time.time() - start
    minutes, seconds = divmod(running,60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d"%(hours, minutes, seconds)
@app.route("/")
def root():
    return f"Hello People! App is running at {elapsed()}"

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=8070)

