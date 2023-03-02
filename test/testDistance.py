import unittest

from Main.fnd.SoundCode.SoundSys.Sound import Sound
from Main.fnd.SoundCode.SoundSys.SoundWrapper import sound_action

sound_obj = Sound([465, 291], 300, "Arrow.wav" , True)

class Test_Distance(unittest.TestCase):
    def test_general(self):
        sound_obj = Sound([765, 291], 300, "Arrow.wav" , True)
        sound_action(sound_obj, [])

    def test_gen2(self):
        sound_obj = Sound([465, 291], 0.2, "Arrow.wav", True)
        sound_obj.create_3d()
        for _ in range(5):
            sound_obj.play()

    def test_move_closer(self):
        sound_obj1 = Sound([465, 291], 20, "Arrow.wav", True)
        sound_obj1.create_3d()
        sound_obj2 = Sound([465, 291], 5, "Arrow.wav", True)
        sound_obj2.create_3d()
        sound_obj3 = Sound([465, 291], 2, "Arrow.wav", True)
        sound_obj3.create_3d()
        sound_obj4 = Sound([465, 291], 0.8, "Arrow.wav", True)
        sound_obj4.create_3d()
        sound_obj5 = Sound([465, 291], 0.2, "Arrow.wav", True)
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
        sound_obj1 = Sound([465, 291], 20, "Arrow.wav", True)
        sound_obj1.create_3d()
        sound_obj2 = Sound([465, 291], 5, "Arrow.wav", True)
        sound_obj2.create_3d()
        sound_obj3 = Sound([465, 291], 2, "Arrow.wav", True)
        sound_obj3.create_3d()
        sound_obj4 = Sound([465, 291], 0.8, "Arrow.wav", True)
        sound_obj4.create_3d()
        sound_obj5 = Sound([465, 291], 0.2, "Arrow.wav", True)
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

if __name__ == '__main__':
    unittest.main()

