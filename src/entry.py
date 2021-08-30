import argparse
import asyncio

import aiohttp
from demo import create_app

try:
	import uvloop
	asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
	print("Uv loop is not installed")
	exit()


parser = argparse.ArgumentParser(description='demo project')
parser.add_argument('--host', help='Host to listen', default='0.0.0.0')
parser.add_argument('--port', help='Port to accept connections', default=5000)
parser.add_argument('--reload', action="store_true" ,help='Autoreload code on change')


args = parser.parse_args()

if args.reload:
	print("Start project with reload")
	app = aiohttp.web.Application()
	import aioreloader
	aioreloader.start()

app = create_app()


if __name__ == '__main__':
	aiohttp.web.run_app(app, host=args.host, port=args.port)