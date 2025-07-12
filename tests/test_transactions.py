from ledger.transaction import log_transaction

def test_log_transaction():
    log_transaction("Alice", "Bob", 10)
    print("Transaction logged successfully.")

if __name__ == "__main__":
    test_log_transaction()
