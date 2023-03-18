import unittest

import Main.Main.fnd.SoundCode.SoundSys.Sound
from Main.Main.fnd.SoundCode.SoundSys.SoundWrapper import sound_action
from Main.Main.fnd.SoundCode.SoundSys.DIST import Fake_Sensor

sound_obj = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 300, "Arrow.wav", True)


# x = 7
# def sensor(op):
#     x = x op 1
#     return x

class Test_Distance(unittest.TestCase):
    def test_general(self):
        sound_obj = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([765, 291], 300, "Arrow.wav", True)
        sound_action(sound_obj)

    def test_gen2(self):
        sound_obj = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 0.2, "Arrow.wav", True)
        sound_obj.create_3d()
        for _ in range(5):
            sound_obj.play()

    def test_move_closer(self):
        sound_obj1 = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 20, "Arrow.wav", True)
        sound_obj1.create_3d()
        sound_obj2 = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 5, "Arrow.wav", True)
        sound_obj2.create_3d()
        sound_obj3 = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 2, "Arrow.wav", True)
        sound_obj3.create_3d()
        sound_obj4 = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 0.8, "Arrow.wav", True)
        sound_obj4.create_3d()
        sound_obj5 = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 0.2, "Arrow.wav", True)
        sound_obj5.create_3d()
        for _ in range(3):
            sound_obj1.play()
        for _ in range(4):
            sound_obj2.play()
        for _ in range(5):
            sound_obj3.play()
        for _ in range(5):
            sound_obj4.play()
        for _ in range(6):
            sound_obj5.play()

    def test_move_away(self):
        sound_obj1 = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 20, "Arrow.wav", True)
        sound_obj1.create_3d()
        sound_obj2 = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 5, "Arrow.wav", True)
        sound_obj2.create_3d()
        sound_obj3 = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 2, "Arrow.wav", True)
        sound_obj3.create_3d()
        sound_obj4 = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 0.8, "Arrow.wav", True)
        sound_obj4.create_3d()
        sound_obj5 = Main.Main.fnd.SoundCode.SoundSys.Sound.Sound([465, 291], 0.2, "Arrow.wav", True)
        sound_obj5.create_3d()
        for _ in range(5):
            sound_obj5.play()
        for _ in range(5):
            sound_obj4.play()
        for _ in range(5):
            sound_obj3.play()
        for _ in range(4):
            sound_obj2.play()
        for _ in range(3):
            sound_obj1.play()

    # TODO: use fake sensor...
    def test_fake_sensor(self):
        fake_sensor = Fake_Sensor(1, True, 0.1)
        print(fake_sensor.sensor())

if __name__ == '__main__':
    unittest.main()

