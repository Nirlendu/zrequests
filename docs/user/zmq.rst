.. _zmq:

ZMQ Adaptor
==============

Introduction
------------
ZMQ Adaptor makes use of the request module to create a HTTP type connection to a ZMQ server. It is completely compliant with the requests module, so it will not hinder any furthur patches in the original requests module. It sends a packet in accordance to the HTTP format to the server, and the server uses the data from the packet

We can initiate the adaptor by::

    import requests
    session = requests.Session()
    adaptor = requests.adapters.ZMQAdapter()

Here we can optimize it using the various options provided

We have to initialise the messaging pattern::

    adaptor.pattern = zmq.REQ

If the server will send json or string, we have to initialise the values to 1, as by default the values are 0::

    adaptor.json = 0
    adaptor.string = 0

The linger option is also included::

    adaptor.linger = 0

High Water Mark too::

    adaptor.hwm = 1

IO_Threads too::

    adaptor.iothreads = 1

And the swap too::

    adaptor.swap = 200*2**10

We have to mount the adaptor and the protocol we need to use::

    s.mount('tcp://', a)

We can make requests in the following fashion, with all the params of the request module::

    resp = session.get("tcp://127.0.0.1:5678", data="test string", timeout=1, auth=HTTPBasicAuth('user', rijndael.encode('something','pass'))

To see the response, just print the response::

    print resp._content




