def test_index_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200


def test_login_with_known_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'john@simplylift.co' in response.data
    
def test_book_page_for_existing_competition(client):
    response = client.get('/book/Spring%20Festival/Simply%20Lift')
    assert response.status_code == 200
    assert b'Spring Festival' in response.data


def test_purchase_places_reduces_available_places(client):
    from server import competitions
    before = int(competitions[0]['numberOfPlaces'])
    client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '2',
    })
    assert int(competitions[0]['numberOfPlaces']) == before - 2


def test_logout_redirects_to_index(client):
    response = client.get('/logout')
    assert response.status_code == 302