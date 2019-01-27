import asyncio
import websockets
import numpy as np
import json
import signal


async def send_number(websocket, path):
    sequence = 1
    try:
        while True:
            await asyncio.sleep(1.5)
            await websocket.send(json.dumps({
                "number": np.random.normal(0, 1),
                "sequence": sequence,
            }))
            sequence += 1
    finally:
        print("end")


async def echo_server(stop):
    async with websockets.serve(send_number, 'localhost', 8765):
        await stop

loop = asyncio.get_event_loop()

# The stop condition is set when receiving SIGTERM.
stop = asyncio.Future()
loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

# Run the server until the stop condition is met.
loop.run_until_complete(echo_server(stop))