from main import main

def test_len():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4]
    assert main(list1) == 5
    assert main(list2) == 4
