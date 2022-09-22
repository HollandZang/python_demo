from json import JSONEncoder
import websocket
import _thread
import time
import json
import __ws__
from __ws__ import WebSocketClient
import asyncio

# websocket.enableTrace(True)
list_token = ['1564521640753643520-mobile','1564521847939678208-mobile']
for i in range(500):
    list_token.append('t_'+str(i))
unit = 'unit'
dict_ws={}

for token in list_token:
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:9527/zhxfz_api/websocket/{}/{}".format(token,unit))
    ws.send("heartbeat")
    dict_ws[token]=ws

time.sleep(3)

send_msg = {
  "key": "sfzh",
  "type": "unit",
  "msg": {
    "topic": "t",
    "group": "g",
    "content": "c"
  }
}

first = dict_ws[list_token[0]]
# first.send(json.dumps(send_msg))
# print(first.recv())

for j in range(10):
    time.sleep(0.2)
    for i in range(100):
        dict_ws[list_token[i]].send(json.dumps(send_msg))

for token,ws in dict_ws.items():
    # ws.send(json.dumps(send_msg))
    print(token,ws.recv())
time.sleep(3)

for token,ws in dict_ws.items():
    ws.close()
