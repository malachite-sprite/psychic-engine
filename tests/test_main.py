from sources import main
import cocos

class TestMain():

    def setup(self):
        cocos.director.director.init()

    def teardown(self):
        cocos.director.director.pop()
    
    def test_vanilla(self):
        #main.main(None) 
        pass

