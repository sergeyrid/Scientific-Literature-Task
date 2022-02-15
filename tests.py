from main import main
from os.path import isfile

all_path = 'test_files/'
in_default_name = 'input.txt'
out_default_name = 'output.txt'
exp_default_name = 'expected.txt'


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


class BaseTestClass:
    @staticmethod
    def run_main_test(test_path: str) -> None:
        main(test_path + in_default_name, test_path + out_default_name)
        check(test_path + exp_default_name, test_path + out_default_name)


class TestDummy(BaseTestClass):
    class_path = all_path + 'dummy_tests/'

    def test1(self) -> None:
        self.run_main_test(self.class_path + 'test1/')

    def test2(self) -> None:
        self.run_main_test(self.class_path + 'test2/')

    def test3(self) -> None:
        self.run_main_test(self.class_path + 'test3/')
