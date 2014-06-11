import requests
s = requests.Session()
a = requests.adapters.ZMQAdapter()
<<<<<<< HEAD
s.mount('tcp://', a)
=======
s.mount('tcp://127.0.0.1:5678', a)
>>>>>>> 278832bca0d6413f63ce6f0ab8a37eafd5c16438
x = s.get('tcp://127.0.0.1:5678')
print x.content
