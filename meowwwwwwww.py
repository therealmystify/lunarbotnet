from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip')
    
    # Perform an ICMP (ping) check
    response = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if response.returncode == 0:
        icmp_status = "Received ICMP"
    else:
        icmp_status = "No ICMP response"
    
    return jsonify({"status": icmp_status})

if __name__ == '__main__':
    app.run(debug=True)
