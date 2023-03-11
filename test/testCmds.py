# import time
# import unittest

# from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state

# state = get_instate_of_state()


# class scan_scenarios(unittest.TestCase):

#     def test_assert_commands_create(self):
#         pass

#     def test_assert_command_change_as_expected(self):
#         state.commandInterface("AA")
#         self.assertEqual(state.get_state(), "pause")
#         state.commandInterface("AA")
#         self.assertEqual(state.get_state(), "Scan")
#         state.commandInterface("A")
#         self.assertEqual(state.get_state(), "dist")
#         state.commandInterface("A")
#         self.assertEqual(state.get_state(), "Scan+ocr")
#         return

#     def test_assert_handle_unknown_cmd(self):
#         # unknown / unmapped command
#         res = state.commandInterface("xyxysyws")
#         self.assertFalse(res)


#     # refernced in our ui/ ux doc
#     def test_user_story_one(self):
#         print("-"*20,"Begin User Story","-"*20)
#         print("User looks around at signs. ")

#         print("User switches to distance mode to see how far sign is away from them? ")
#         state.commandInterface("A")
#         print("User mistakenly enters text mode. ")
#         state.commandInterface("A")
#         time.sleep(2)
#         print("User trys again & pauses")
#         state.commandInterface("AA")
#         time.sleep(2)
#         print("User resumes to text mode")
#         state.commandInterface("AA")
#         time.sleep(2)
#         print("User pauses this reading")
#         state.commandInterface("AA")
#         time.sleep(2)
#         print("User turns volume down")
#         state.commandInterface("B")

#         return


# if __name__ == '__main__':
#     unittest.main()
