from flask import Flask, request, jsonify
from biometric.utils import generate_biometric_hash
from lvp.calculate_lvp import calculate_lvp
from ledger.transaction import log_transaction

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    bio_hash = generate_biometric_hash(data['face'], data['voice'])
    return jsonify({'ubid': bio_hash})

@app.route('/earn-lvp', methods=['POST'])
def earn_lvp():
    data = request.json
    lvp = calculate_lvp(data['hours'], data['skill_weight'], data['region_factor'])
    return jsonify({'lvp_earned': lvp})

@app.route('/transact', methods=['POST'])
def transact():
    data = request.json
    log_transaction(data['from'], data['to'], data['amount'])
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
