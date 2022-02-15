from main import main
from os.path import isfile
from pytest import raises
from typing import Any

all_path = 'test_files/'
in_default_name = 'input.txt'
out_default_name = 'output.txt'
exp_default_name = 'expected.txt'


class BaseTestClass:
    @staticmethod
    def check(exp_name: str, out_name: str) -> None:
        assert isfile(exp_name)
        assert isfile(out_name)
        expected = []
        with open(exp_name, 'r') as exp_file:
            for line in exp_file.readlines():
                try:
                    expected.append(int(line))
                except ValueError:
                    raise ValueError('Incorrect expected file format')
        output = []
        with open(out_name, 'r') as out_file:
            for line in out_file.readlines():
                try:
                    output.append(int(line))
                except ValueError:
                    raise ValueError('Incorrect output file format')
        assert output == expected

    @staticmethod
    def check_exception(test_path: str, exception: Any) -> None:
        with raises(exception):
            main(test_path + in_default_name, test_path + out_default_name)

    def run_main_test(self, test_path: str) -> None:
        main(test_path + in_default_name, test_path + out_default_name)
        self.check(test_path + exp_default_name, test_path + out_default_name)


class TestDummy(BaseTestClass):
    class_path = all_path + 'dummy_tests/'

    def test1(self) -> None:
        self.run_main_test(self.class_path + 'test1/')

    def test2(self) -> None:
        self.run_main_test(self.class_path + 'test2/')

    def test3(self) -> None:
        self.run_main_test(self.class_path + 'test3/')


class TestIncorrectInput(BaseTestClass):
    class_path = all_path + 'incorrect_input_tests/'

    def test_empty_file(self) -> None:
        self.check_exception(self.class_path + 'test_empty_file/', ValueError)

    def test_incomplete_file(self) -> None:
        self.check_exception(self.class_path + 'test_empty_file/', ValueError)

    def test_letters_in_file(self) -> None:
        self.check_exception(self.class_path + 'test_letters_in_file/', ValueError)

    def test_negative_values(self) -> None:
        self.check_exception(self.class_path + 'test_negative_values/', ValueError)

    def test_no_file(self) -> None:
        self.check_exception(self.class_path + 'test_no_file/', FileNotFoundError)

    def test_not_enough_edges(self) -> None:
        self.check_exception(self.class_path + 'test_not_enough_edges/', ValueError)

    def test_too_big_values(self) -> None:
        self.check_exception(self.class_path + 'test_too_big_values/', ValueError)


class TestBorderlineCases(BaseTestClass):
    class_path = all_path + 'borderline_cases_tests/'

    def test_complete_graph(self) -> None:
        self.run_main_test(self.class_path + 'test_complete_graph/')

    def test_empty_answer(self) -> None:
        self.run_main_test(self.class_path + 'test_empty_answer/')

    def test_empty_graph(self) -> None:
        self.run_main_test(self.class_path + 'test_empty_graph/')

    def test_empty_set1(self) -> None:
        self.run_main_test(self.class_path + 'test_empty_set1/')

    def test_empty_set2(self) -> None:
        self.run_main_test(self.class_path + 'test_empty_set2/')

    def test_empty_sets(self) -> None:
        self.run_main_test(self.class_path + 'test_empty_sets/')

    def test_no_edges(self) -> None:
        self.run_main_test(self.class_path + 'test_no_edges/')

    def test_sets_intersect(self) -> None:
        self.run_main_test(self.class_path + 'test_sets_intersect/')
