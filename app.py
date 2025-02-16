import os
import platform
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip', '8.8.8.8')
    
    # Choose the appropriate ping command based on the OS
    system_name = platform.system().lower()
    if system_name == 'windows':
        # Windows uses -n for count and 'nul' to discard output
        cmd = f"ping -n 1 {ip} > nul"
    else:
        # Unix-based systems use -c for count and /dev/null to discard output
        cmd = f"ping -c 1 {ip} > /dev/null 2>&1"
    
    response = os.system(cmd)
    
    # os.system returns 0 on success, non-zero on failure
    return jsonify({"ip": ip, "reachable": response == 0})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
