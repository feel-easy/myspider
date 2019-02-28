from quart import Quart, websocket
app = Quart(__name__)

@app.route('/')
async def hello():
    return 'abcdefghijklmnopqrstuvwxyz'

app.run()