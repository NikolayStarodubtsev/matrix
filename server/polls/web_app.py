import sys
sys.path.append("../../")

from aiohttp import web

from server.polls import routes


if __name__ == "__main__":
    app = web.Application()
    routes.setup_routes(app)
    web.run_app(app)
