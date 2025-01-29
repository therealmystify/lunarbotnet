import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip', '8.8.8.8')
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    return jsonify({"ip": ip, "reachable": response == 0})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)