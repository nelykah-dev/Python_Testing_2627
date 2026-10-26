import server


def test_index_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200


def test_login_with_known_email(client):
    response = client.post('/showSummary',
                           data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'john@simplylift.co' in response.data


def test_book_page_for_existing_competition(client):
    response = client.get('/book/Spring%20Festival/Simply%20Lift')
    assert response.status_code == 200
    assert b'Spring Festival' in response.data


def test_purchase_places_reduces_available_places(client, monkeypatch):
    comps = [{'name': 'Future Cup', 'date': '2030-01-01 10:00:00',
              'numberOfPlaces': '10'}]
    cl = [{'name': 'Test Club', 'email': 't@t.co', 'points': '5'}]
    monkeypatch.setattr(server, 'competitions', comps)
    monkeypatch.setattr(server, 'clubs', cl)
    monkeypatch.setattr(server, 'bookings', {})
    client.post('/purchasePlaces', data={
        'club': 'Test Club', 'competition': 'Future Cup', 'places': '2'})
    assert comps[0]['numberOfPlaces'] == 8
    assert cl[0]['points'] == 3


def test_logout_redirects_to_index(client):
    response = client.get('/logout')
    assert response.status_code == 302


def test_points_page_is_public(client):
    response = client.get('/points')
    assert response.status_code == 200