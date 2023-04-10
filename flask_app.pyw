from flask import Flask
import os
import sys

# Get the full path to the script.pyw file in the root directory
script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "script.pyw"))

# Add the directory containing script.pyw to the Python module search path
sys.path.append(os.path.dirname(script_path))

# Import the script module
import script
import threading

app = Flask(__name__)

def run_script_in_thread():
    script_thread = threading.Thread(target=script.run)
    script_thread.start()

@app.route('/')
def run_script():
    run_script_in_thread()
    return "Script executed"

if __name__ == '__main__':
    app.run()
