def test_index_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200


def test_login_with_known_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'john@simplylift.co' in response.data