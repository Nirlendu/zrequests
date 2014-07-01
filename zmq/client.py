import requests
import zmq

def a():
    session = requests.Session()
    adaptor = requests.adapters.ZMQAdapter()
    #adaptor.multipart=1
    adaptor.pattern = zmq.REQ
    adaptor.json = 1
    adaptor.string = 0
    adaptor.linger = 0
    adaptor.hwm = 1
    adaptor.iothreads = 1
    adaptor.swap = 200*2**10
    session.mount('tcp://', adaptor)
    resp = session.get("tcp://127.0.0.1:5678", data="test string", timeout=1)
    print resp.raw


def b():
    session = requests.Session()
    adaptor = requests.adapters.ZMQAdapter()
    adaptor.pattern = zmq.SUB
    adaptor.subscribe='germany'
    session.mount('tcp://', adaptor)
    resp = session.get("tcp://127.0.0.1:5679")
    print resp.raw



a()
