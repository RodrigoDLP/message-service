import datetime
from message_service.api_receiver import process_transaction
from schemas import RawTransaction

def test_process_transaction_new_user():
    tx = RawTransaction(
        amount=200,
        creditcard=1234567890123456,
        codigo="XYZ789",
        email="newuser@example.com",
        datetime=datetime.datetime.now()
    )
    result = process_transaction(tx)
    assert result.original_amount == 200
    assert result.final_amount in (200, 100)  # depende de puntos
    assert result.email == "newuser@example.com"

def test_process_transaction_no_email():
    tx = RawTransaction(
        amount=50,
        creditcard=9876543210987654,
        codigo="NOEMAIL",
        email=None,
        datetime=datetime.datetime.now()
    )
    result = process_transaction(tx)
    assert result.original_amount == 50
    assert result.final_amount == 50
    assert result.email is None
