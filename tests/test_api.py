import datetime

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_register_transaction(client):
    payload = {
        "amount": 150,
        "creditcard": 1234567890123456,
        "codigo": "ABC123",
        "email": "test@example.com",
        "datetime": datetime.datetime.now().isoformat()
    }
    response = client.post("/register-transaction", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "sent"
    assert data["transaction"]["amount"] == 150

def test_get_payments(client):
    response = client.get("/payments")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
