import json
import os

def log_transaction(sender, receiver, lvp):
    ledger_path = os.path.join(os.path.dirname(__file__), 'ledger.json')
    with open(ledger_path, 'r+') as f:
        ledger = json.load(f)
        ledger.append({
            'from': sender,
            'to': receiver,
            'amount': lvp,
            'status': 'confirmed'
        })
        f.seek(0)
        json.dump(ledger, f, indent=2)
