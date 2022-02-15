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
            if line.isnumeric():
                expected.append(int(line))
    output = []
    with open(out_name, 'r') as out_file:
        for line in out_file.readlines():
            if line.isnumeric():
                output.append(int(line))
    assert expected == output


class TestDummy:
    dummy_path = all_path + 'dummy_tests/'

    def test1(self) -> None:
        test1_path = self.dummy_path + 'test1/'
        main(test1_path + in_default_name, test1_path + out_default_name)
        check(test1_path + exp_default_name, test1_path + out_default_name)

    def test2(self) -> None:
        test2_path = self.dummy_path + 'test2/'
        main(test2_path + in_default_name, test2_path + out_default_name)
        check(test2_path + exp_default_name, test2_path + out_default_name)

    def test3(self) -> None:
        test3_path = self.dummy_path + 'test3/'
        main(test3_path + in_default_name, test3_path + out_default_name)
        check(test3_path + exp_default_name, test3_path + out_default_name)
