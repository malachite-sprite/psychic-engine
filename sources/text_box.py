import cocos
import pyglet
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class TextBox(cocos.layer.Layer):
    """A cocos layer that captures and displays keyboard input. Optionally,
    it acts when an "enter" key is pressed; calling a given function with 
    the text as a parameter and then clearing the text
    """

    is_event_handler = True

    def __init__(self, enter_function=None):
        super(TextBox, self).__init__()
        
        self.label = cocos.text.Label("", x=100, y=280)
        self.text = list()
        self.enter_function = enter_function

        self.update_label()
        self.add(self.label)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.BACKSPACE:
            try:
                self.text.pop()
            except IndexError:
                pass
        elif symbol == pyglet.window.key.ENTER:
            if self.enter_function:
                logger.debug("calling enter function")
                self.enter_function("".join(self.text))
                self.text = list()
        else:
            self.text.append(chr(symbol))#pyglet.window.key.symbol_string(symbol)) 
        self.update_label()

    def on_key_release(self, symbol, modifiers):
        pass

    def update_label(self):
        if len(self.text) == 0:
            self.label.element.text = ""
        else:
            self.label.element.text = "".join(self.text)

if __name__ == '__main__':
    cocos.director.director.init(resizable=True)
    # Run a scene with our event displayers:
    cocos.director.director.run(cocos.scene.Scene(TextBox()))

