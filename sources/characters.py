import cocos

root_bone = cocos.skeleton.Bone('body', 60, -180.0, (0.0, 0.0)
#).add(
#    cocos.skeleton.Bone('head', 20, 0, (0, -60))
).add(
    cocos.skeleton.Bone('l_upperarm', 30, 120, (0, -60)).add(
        cocos.skeleton.Bone('l_forearm', 30, 30, (0, -30)) 
    )
).add(
    cocos.skeleton.Bone('r_upperarm', 30, -140, (0, -60)).add(
        cocos.skeleton.Bone('r_forearm', 30, 30, (0, -30))
    )
).add(
    cocos.skeleton.Bone('l_thigh', 35, 170, (0, 0)).add(
        cocos.skeleton.Bone('l_calf', 35, -10, (0, -35))
    )
).add(
    cocos.skeleton.Bone('r_thigh', 35, -160, (0, 0)).add(
        cocos.skeleton.Bone('r_calf', 35, -20, (0, -35))
    )
)

char_skeleton = cocos.skeleton.Skeleton(root_bone)

char_skins = None
#[
#    (bone_name, (off, set), 'some.image', flipped-x?, flipped-y?, scale_factor),
#]

class Character():
    def __init__(self):
        # just for testing purposes..
        # self.skin = cocos.skeleton.BitmapSkin(char_skeleton, skin)
        self.skin = cocos.skeleton.ColorSkin(char_skeleton, (255,255,255,255))

        x,y = cocos.director.director.get_window_size()
        self.skin.position = x/2, y/2

if __name__ == '__main__':
    cocos.director.director.init(resizable=True)
    layer = cocos.layer.Layer()
    layer.add(Character().skin)
    cocos.director.director.run(cocos.scene.Scene(layer))
