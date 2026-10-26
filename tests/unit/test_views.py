import pytest
import server


@pytest.fixture
def fake_data(monkeypatch):
    clubs = [{'name': 'Test Club', 'email': 't@t.co', 'points': '5'}]
    competitions = [{'name': 'Test Cup', 'date': '2030-01-01 10:00:00',
                     'numberOfPlaces': '10'}]
    monkeypatch.setattr(server, 'clubs', clubs)
    monkeypatch.setattr(server, 'competitions', competitions)
    monkeypatch.setattr(server, 'bookings', {})
    return clubs, competitions

def purchase(places):
    with server.app.test_request_context(
            '/purchasePlaces', method='POST',
            data={'club': 'Test Club', 'competition': 'Test Cup',
                  'places': str(places)}):
        return server.purchasePlaces()


def test_logout_returns_redirect_response():
    with server.app.test_request_context('/logout'):
        response = server.logout()
    assert response.status_code == 302


def test_purchase_removes_places_from_competition(fake_data):
    _, competitions = fake_data
    purchase(3)
    assert competitions[0]['numberOfPlaces'] == 7


def test_purchase_one_place_leaves_nine(fake_data):
    _, competitions = fake_data
    purchase(1)
    assert competitions[0]['numberOfPlaces'] == 9


def test_purchase_two_times_adds_up(fake_data):
    _, competitions = fake_data
    purchase(2)
    purchase(3)
    assert competitions[0]['numberOfPlaces'] == 5


def test_purchase_returns_confirmation_message(fake_data):
    html = purchase(2)
    assert 'Great-booking complete!' in html


def test_show_summary_with_known_email(fake_data):
    with server.app.test_request_context(
            '/showSummary', method='POST', data={'email': 't@t.co'}):
        html = server.showSummary()
    assert 't@t.co' in html


def test_index_returns_login_page():
    with server.app.test_request_context('/'):
        html = server.index()
    assert 'GUDLFT Registration' in html


def test_book_returns_booking_page(fake_data):
    with server.app.test_request_context('/book/Test Cup/Test Club'):
        html = server.book('Test Cup', 'Test Club')
    assert 'Test Cup' in html