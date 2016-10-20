from server.polls import views


def setup_routes(app):
    app.router.add_get('/', views.hello)
    app.router.add_post('/find_prime', views.find_n_prime)
    app.router.add_post('/factorize', views.factorization)
    app.router.add_post('/ping', views.ping_server)
