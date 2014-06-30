import requests
import zmq
session = requests.Session()
adaptor = requests.adapters.ZMQAdapter()
#adaptor.multipart=1
adaptor.pattern = zmq.REQ
session.mount('tcp://', adaptor)
resp = session.get("tcp://127.0.0.1:5678", data="test string", timeout=1)
print resp.raw
"""
adaptor.pattern = zmq.SUB
session.mount('tcp://', adaptor)
resp = session.get("tcp://127.0.0.1:5679", timeout=1)
print resp.raw
"""
