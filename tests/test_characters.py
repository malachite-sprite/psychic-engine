from sources import characters
import cocos

class TestCharacters():

    def setup(self):
        cocos.director.director.init()
    
    def teardown(self):
        cocos.director.director.pop()

    def test_vanilla(self):
        MyCharacter = characters.Character() 
        layer = cocos.layer.Layer()
        layer.add(MyCharacter.skin)

if __name__ == '__main__':
    Cls = TestCharacters()
    Cls.setup()
    Cls.test_vanilla()
    Cls.teardown()
