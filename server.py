from flask import Flask, render_template, redirect
import subprocess
import os
import time

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index_page():
    return render_template("index.html")

@app.route("/startapp")
def start_streamlit():
    streamlit_file_path = os.path.join("streamlit", "2.py")
    streamlit_process = subprocess.Popen(["streamlit", "run", streamlit_file_path, "--server.port", "8501"])
    time.sleep(5)
    return redirect("http://localhost:8501")

@app.route("/error")
def err_page():
    return render_template("why.html")

if __name__ == "__main__":
    app.run(debug=True)