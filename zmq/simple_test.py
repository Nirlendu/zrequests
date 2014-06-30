import requests
import zmq
session = requests.Session()
adaptor = requests.adapters.ZMQAdapter()
adaptor.pattern = zmq.REQ
session.mount('tcp://', adaptor)
resp = session.get("tcp://127.0.0.1:5678", data="test string", timeout=1)
print resp.raw
