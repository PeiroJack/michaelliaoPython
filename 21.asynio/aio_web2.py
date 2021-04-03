#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aiohttp import web
import asyncio

# 根据 Web Server Quickstart 进行了一些修改，看起来更简洁易懂：
# https://docs.aiohttp.org/en/stable/web_quickstart.html
routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
    await asyncio.sleep(2)
    return web.Response(body='<h1>Index</h1>'.encode(), content_type='text/html')

@routes.get('/hello/{name}')
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

app = web.Application()
app.add_routes(routes)
web.run_app(app)