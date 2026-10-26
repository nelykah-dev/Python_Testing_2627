from server import loadClubs, loadCompetitions


def test_load_clubs_returns_three_clubs():
    clubs = loadClubs()
    assert len(clubs) == 3


def test_load_competitions_have_required_keys():
    for competition in loadCompetitions():
        assert 'name' in competition
        assert 'date' in competition
        assert 'numberOfPlaces' in competition