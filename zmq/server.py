import zmq


req_rep_context = zmq.Context()
req_rep_sock = req_rep_context.socket(zmq.REP)
req_rep_sock.bind("tcp://127.0.0.1:5678")
while True:
    message = req_rep_sock.recv()
    print message
    req_rep_sock.send(message)


"""
context = zmq.Context()
pub_sub_sock = context.socket(zmq.PUB)
pub_sub_sock.bind("tcp://127.0.0.1:5679")
i=0
while i < 10:
    string = pub_sub_sock.send_multipart(str(i))
    i=i+1
"""
