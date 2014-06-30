import zmq

# ZeroMQ Context
req_rep_context = zmq.Context()
"""
push_pull_context = zmq.Context()
router_dealer_context = zmq.Context()
pub_sub_context = zmq.Context()
"""


# Define the socket using the "Context"
req_rep_sock = req_rep_context.socket(zmq.REP)
"""
push_pull_sock = push_pull_context.socket(zmq.PUSH)
router_dealer_sock = router_dealer_context.socket(zmq.DEALER)
pub_sub_sock = pub_sub_context.socket(zmq.PUB)
"""


req_rep_sock.bind("tcp://127.0.0.1:5678")
"""
push_pull_sock()
router_dealer_sock()
pub_sub_sock()
"""

# Run a simple "Echo" server
while True:
    message = req_rep_sock.recv()
    print message
    req_rep_sock.send(message)
