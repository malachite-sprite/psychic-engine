import wit
import logging
import uuid

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

wit_logger = logging.getLogger("wit")
wit_logger.setLevel(logging.DEBUG)

class Conversation():
    """A class that encapsulates all of things NLP. 

    Currently, it uses wit.ai (https://github.com/wit-ai/pywit), which
    requires sending the text to their servers for processing. This
    class handles the tokens and authentication for that, as well as
    the various action calls.

    This also stores the context of the current conversation.
    """ 

    def __init__(self, actions=None):
        self.access_token = "IYMTZME22PFSSPFSEAJ2XVNTS5ZZ6632"
        self.actions = actions or {
            'send': self.send,
            'act': self.act,
        }
        self.session_id = uuid.uuid1() # any unique string
        self.context = {}

        self.WitClient = wit.Wit(
                self.access_token, self.actions, logging.getLogger("wit")
        )

    def send_message(self, message):
        self.context = self.WitClient.run_actions(
                self.session_id, message, context=self.context
        )
    
    def send(self, request, response):
        print("message recieved: " + str(response['text']))

    def act(self, request):
        logger.debug(request['entities'])
        return request['context']

