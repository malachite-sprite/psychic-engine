from sources import wit_handler
import wit
import logging
import pytest_mock as mocker
import pytest_capturelog as caplog


class MockWitClass(wit.Wit):

    def __init__(self, access_token, actions=None, logger=None):
        super(MockWitClass, self).__init__(access_token, actions, logger)

    def __init__(self, wit_client):
        super(MockWitClass, self).__init__(
                wit_client.access_token,
                wit_client.actions,
                wit_client.logger,
        )

    def run_actions(self, session_id, message, context=None,
                    max_steps=5, verbose=None):
        self.actions["send"](request=None, reponse=None)
        self.actions["act"](request=None)
        
class TestWitHandler():
    
    def test_vanilla(self):
        Convo = wit_handler.Conversation()

    def test_new_actions(self, mocker):
        act = mocker.stub(name="act")
        send = mocker.stub(name="send")
        actions = {"act": act, "send": send}
        Convo = wit_handler.Conversation(actions)
        Convo.WitClient = MockWitClass(Convo.WitClient)
        Convo.send_message("anne, do the thing")
        assert send.call_count == 1
        assert act.call_count == 1

    def test_default_send(self, capsys):
        Convo = wit_handler.Conversation()
        Convo.send(request=None, response={"text": "hello world"})
        out, __ = capsys.readouterr()
        assert "hello world" in out

    def test_default_act(self, caplog):
        caplog.setLevel(logging.DEBUG)
        Convo = wit_handler.Conversation()
        context = Convo.act(request={
                    'entities': 'some_entities',
                    'context': 'some_context',
                },
        )
        assert "some_entities" in caplog.text()
        assert context == 'some_context'

