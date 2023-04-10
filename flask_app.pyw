from flask import Flask
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
