import jinja2
import aiohttp_jinja2
import urllib.parse as up
import asyncpg

from aiohttp import web

from .routes import setup_routes
from .config import config_obj as config



async def on_start(app):
	up.uses_netloc.append("postgres")
	url = up.urlparse(config['database_url'])
	connection = await asyncpg.connect(user=url.username,
									   password=url.password,
                                       database=url.path[1:],
                                       host=url.hostname,
                                       port=url.port)
	config['db'] = connection
	print("Connected to db!")


async def create_app():
	app = web.Application()
	aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('demo', 'templates'))
	setup_routes(app)
	await on_start(app)
	return app
