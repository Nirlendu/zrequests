import json
import random
import string

import requests

from pytest import fixture, raises, fail


@fixture(scope="module")
def session():
    """Returns ZMQ sever connection instance"""

    session = requests.Session()
    adaptor = requests.adapters.ZMQAdapter()
    adaptor.pattern = 'req_rep'
    session.mount('tcp://', adaptor)

    return session


@fixture(scope="function")
def rand():
    return ''.join([random.choice(string.ascii_lowercase) for i in range(10)])


class TestZMQ:

    def test_response_status_code(self, session, rand):
        resp = session.get("tcp://127.0.0.1:5678", data=rand, timeout=1)
        assert 200 == resp.status_code

    def test_response_content(self, session, rand):
        resp = session.get("tcp://127.0.0.1:5678", data=rand, timeout=1)
        assert rand == resp.raw

    def test_response_valid_json(self, session):
        data = {u"name": u"Darth Vader"}
        payload = json.dumps(data)
        resp = session.get("tcp://127.0.0.1:5678", data=payload, timeout=1)

        try:
            resp.json()
        except ValueError:
            fail("Response is not a valid json")

        assert data == resp.json()

    def test_response_invalid_json(self, session, rand):
        data = 'Let the source be with you, Luke'
        resp = session.get("tcp://127.0.0.1:5678", data=data, timeout=1)

        with raises(ValueError):
            resp.json()
