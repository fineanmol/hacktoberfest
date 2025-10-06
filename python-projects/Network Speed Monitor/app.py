from flask import Flask, render_template, jsonify
from network_speed_monitor import test_speed, log_to_csv, log_to_json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test-speed', methods=['GET'])
def speed_test():
    result = test_speed()
    log_to_csv(result)
    log_to_json(result)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
