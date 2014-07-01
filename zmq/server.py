import zmq

def a():
    import json
    req_rep_context = zmq.Context()
    req_rep_sock = req_rep_context.socket(zmq.REP)
    req_rep_sock.bind("tcp://127.0.0.1:5678")
    a=json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    while True:
        message = req_rep_sock.recv()
        print message
        #req_rep_sock.send(message)
        #req_rep_sock.send_string(message)
        req_rep_sock.send_json(a)

def b():
    from random import choice
    import time
    countries = ['netherlands','brazil','germany','portugal']
    events = ['yellow card', 'red card', 'goal', 'corner', 'foul']
    context = zmq.Context()
    pub_sub_sock = context.socket(zmq.PUB)
    pub_sub_sock.bind("tcp://127.0.0.1:5679")
    while True:
        time.sleep(2)
        msg = choice( countries ) +" "+ choice( events )
        print "->",msg
        pub_sub_sock.send( msg )


a()
