import os
import functions as fc
import unittest

if __name__ == '__main__':
    unittest.main()


class TestAnswers(unittest.TestCase):
    def test_answer_yes(self):
        self.assertTrue(fc.answer_yes_or_no("s"))
        self.assertTrue(fc.answer_yes_or_no("S"))
        self.assertTrue(fc.answer_yes_or_no("sim"))
        self.assertTrue(fc.answer_yes_or_no("Sim"))

    def test_answer_no(self):
        self.assertFalse(fc.answer_yes_or_no("n"))
        self.assertFalse(fc.answer_yes_or_no("N"))
        self.assertFalse(fc.answer_yes_or_no("não"))
        self.assertFalse(fc.answer_yes_or_no("Não"))
        self.assertFalse(fc.answer_yes_or_no("nao"))
        self.assertFalse(fc.answer_yes_or_no("Nao"))


class TestComputeFinalTime(unittest.TestCase):
    def test_compute_final_time_with_integers(self):
        self.assertEqual(fc.compute_final_time(20000, "test"), (5, 33, 20.0))

    def test_compute_final_time_with_float(self):
        self.assertEqual(fc.compute_final_time(16790.355, "test"), (4, 39, 50.355))

    def test_compute_final_time_with_more_than_3_numbers_float(self):
        self.assertEqual(fc.compute_final_time(15590.3813214, "test"), (4, 19, 50.381))

    def test_compute_final_time_with_round_float(self):
        self.assertEqual(fc.compute_final_time(15590.38378932, "test"), (4, 19, 50.384))


class TestSkipSceneCommand(unittest.TestCase):
    def test_skipscene_command_based_on_os_system(self):
        if os.name in ('nt', 'dos'):
            self.assertEqual(fc.skip(1, "command"), 'cls')
        else:
            self.assertEqual(fc.skip(1, "command"), 'clear')


class TestTryMenu(unittest.TestCase):
    def test_try_menu_have_to_open_menu(self):
        self.assertEqual(fc.try_menu("menu", "test"), "Open")
        self.assertEqual(fc.try_menu("Menu", "test"), "Open")
        self.assertEqual(fc.try_menu("pause", "test"), "Open")
        self.assertEqual(fc.try_menu("Pause", "test"), "Open")

    def test_try_menu_have_to_pass(self):
        self.assertEqual(fc.try_menu("", "test"), "Pass")
        self.assertEqual(fc.try_menu("pass", "test"), "Pass")
        self.assertEqual(fc.try_menu("1", "test"), "Pass")
        self.assertEqual(fc.try_menu("enter", "test"), "Pass")
