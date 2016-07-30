from sources import text_box
import pytest_mock as mocker
import cocos
import pyglet

class TestTextBox():

    cocos.director.director.init()

    def mock_key_pressed(self, box, string):
        for char in string:
            box.on_key_press(ord(char), None)

    def mock_key_released(self, box, string):
        for char in string:
            box.on_key_release(ord(char), None)

    def mock_enter_pressed(self, box):
        box.on_key_press(pyglet.window.key.ENTER, None)

    def mock_backspace_pressed(self, box):
        box.on_key_press(pyglet.window.key.BACKSPACE, None)

    def test_vanilla(self):
        box = text_box.TextBox()
        self.mock_key_pressed(box, "hello world")
        assert "".join(box.text) == "hello world"
        assert box.label.element.text == "hello world"

    def test_key_press_release(self):
        box = text_box.TextBox()
        self.mock_key_pressed(box, "a")
        self.mock_key_released(box, "a")
        assert box.label.element.text == "a"

    def test_enter_function(self, mocker):
        stub = mocker.stub(name="enter_function")
        box = text_box.TextBox(enter_function=stub)
        self.mock_key_pressed(box, "hello world")
        self.mock_enter_pressed(box)
        assert box.label.element.text == ""
        stub.assert_called_once_with("hello world")

    def test_backspace(self):
        box = text_box.TextBox()
        self.mock_key_pressed(box, "hello")
        self.mock_backspace_pressed(box)
        assert box.label.element.text == "hell"

    def test_backspace_handle(self):
        box = text_box.TextBox()
        self.mock_backspace_pressed(box)

