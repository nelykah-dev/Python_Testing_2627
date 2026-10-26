from locust import HttpUser, task, between


class ClubSecretary(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def load_login_page(self):
        self.client.get('/', name='load /')

    @task(3)
    def log_in(self):
        self.client.post('/showSummary',
                         data={'email': 'john@simplylift.co'},
                         name='load /showSummary')

    @task(2)
    def load_booking_page(self):
        self.client.get('/book/Spring%20Festival/Simply%20Lift',
                        name='load /book')

    @task(1)
    def purchase_places(self):
        self.client.post('/purchasePlaces',
                         data={'club': 'Simply Lift',
                               'competition': 'Spring Festival',
                               'places': '1'},
                         name='update /purchasePlaces')