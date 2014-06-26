.. _zmq:

ZMQ Adaptor
==============

This adapter is designed to communicate with a zmq server using python requests.
We can do so in the following manner::

	>>> import requests
	>>> session = requests.Session()
    >>> adapter = requests.adapters.ZMQAdapter()

Now we need to specify the messaging pattern to communicate with the server. As ZMQ supports many messaging patterns, we can easily
configure the connection according to our needs. Right now, only four patterns are implemented::
	
	'req_rep' 		: 	 Request - Reply
	'pub_sub' 		: 	 Publisher - Subscriber
	'push_pull' 	:	 Push - Pull
	'router_dealer'	:	 Router - Dealer

We have to specify the pattern we would like to use in the following manner::

    >>> adapter.pattern = 'req_rep'

Then, we have to mount it on the session, after specifying the protocol to be used::

    >>> session.mount('tcp://', adapter)

After mounting, we can use this specific request session to make requests and get appropriate response

	>>> session.get("tcp://127.0.0.1:5678", data=rand, timeout=1)

Here, data stands for the data we want to send the server and timeout is for the duration for which the client waits for the connection
from the server. 
Accordingly, the status code will be reflected upon. 
