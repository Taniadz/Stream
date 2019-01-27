import asyncio
import websockets
import numpy
import json
from datetime import datetime

number_array = []


def check_deviation(normal_number):
    number_array.append(normal_number)
    numpy_array = numpy.array(number_array)
    mean = numpy.mean(numpy_array)
    sd = numpy.std(numpy_array)

    if sd != 0:
        deviation = (mean - normal_number) / sd
        if deviation > 2:
            return True
        else:
            return False


async def receive_number():
    async with websockets.connect(
            'ws://localhost:8765',
    ) as websocket:
        while True:
            data = await websocket.recv()
            text_data_json = json.loads(data)

            normal_number = text_data_json.get("number")
            if check_deviation(normal_number):
                print(normal_number)
                async with websockets.connect(
                        'ws://localhost:8000/ws/chat/alert/',
                ) as websocket_django:
                    await websocket_django.send(json.dumps(
                        {'number': normal_number,
                         'sequence': text_data_json.get("sequence"),
                         "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}))


asyncio.get_event_loop().run_until_complete(receive_number())
