import logging

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(format=log_format)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

import cocos
from sources import text_box
from sources import wit_handler
import argparse


def main(args):
    """Get this bird off the ground!"""

    cocos.director.director.init(resizable=True)

    Conversation = wit_handler.Conversation()
    TextBox = text_box.TextBox(
        enter_function=Conversation.send_message
    )

    # Run a scene with our event displayers:
    cocos.director.director.run(cocos.scene.Scene(TextBox))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
