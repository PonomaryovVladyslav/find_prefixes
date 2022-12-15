from unittest import TestCase

from main import FindPrefixes, EmptyInput


class TestGetEndAndMid(TestCase):
    def test_empty_input(self):
        fp = FindPrefixes([])
        end, mid = fp.get_end_and_mid(0, None)
        self.assertEqual(mid, 0)
        self.assertEqual(end, 0)

    def test_one_element_input(self):
        fp = FindPrefixes(['a'])
        end, mid = fp.get_end_and_mid(0, None)
        self.assertEqual(mid, 0)
        self.assertEqual(end, 1)

    def test_odd_elements(self):
        fp = FindPrefixes(['a', 'b', 'c', 'd'])
        end, mid = fp.get_end_and_mid(0, None)
        self.assertEqual(mid, 2)
        self.assertEqual(end, 4)

    def test_even_elements(self):
        fp = FindPrefixes(['a', 'b', 'c', 'd', 'e'])
        end, mid = fp.get_end_and_mid(0, None)
        self.assertEqual(mid, 2)
        self.assertEqual(end, 5)


class TestIsLeftFirst(TestCase):
    def test_move_left_input(self):
        fp = FindPrefixes(['aa', 'ab', 'aba', 'abc', 'addd'], 'ab')
        is_left_0 = fp.is_left_first(0)
        is_left_1 = fp.is_left_first(1)
        is_left_2 = fp.is_left_first(2)
        is_left_3 = fp.is_left_first(3)
        self.assertFalse(is_left_0)
        self.assertTrue(is_left_1)
        self.assertTrue(is_left_2)
        self.assertTrue(is_left_3)

    def test_move_right(self):
        fp = FindPrefixes(['aab', 'aab', 'aaba', 'abddd', 'addddd'], 'ab')
        is_left_0 = fp.is_left_first(0)
        is_left_1 = fp.is_left_first(1)
        is_left_2 = fp.is_left_first(2)
        is_left_3 = fp.is_left_first(3)
        self.assertFalse(is_left_0)
        self.assertFalse(is_left_1)
        self.assertFalse(is_left_2)
        self.assertTrue(is_left_3)


class TestIsLeftLast(TestCase):
    def test_move_left_input(self):
        fp = FindPrefixes(['aa', 'ab', 'aba', 'abc', 'addd', 'bbbb', 'ccccc'], 'ab')
        is_left_0 = fp.is_left_last(0)
        is_left_1 = fp.is_left_last(1)
        is_left_2 = fp.is_left_last(2)
        is_left_3 = fp.is_left_last(3)
        is_left_4 = fp.is_left_last(4)
        is_left_5 = fp.is_left_last(5)
        self.assertFalse(is_left_0)
        self.assertFalse(is_left_1)
        self.assertFalse(is_left_2)
        self.assertFalse(is_left_3)
        self.assertTrue(is_left_4)
        self.assertTrue(is_left_5)

    def test_move_right(self):
        fp = FindPrefixes(['aab', 'aab', 'aaba', 'abddd', 'addddd', 'bbbbb', 'ccccc'], 'ab')
        is_left_0 = fp.is_left_last(0)
        is_left_1 = fp.is_left_last(1)
        is_left_2 = fp.is_left_last(2)
        is_left_3 = fp.is_left_last(3)
        is_left_4 = fp.is_left_last(4)
        is_left_5 = fp.is_left_last(5)
        self.assertFalse(is_left_0)
        self.assertFalse(is_left_1)
        self.assertFalse(is_left_2)
        self.assertFalse(is_left_3)
        self.assertTrue(is_left_4)
        self.assertTrue(is_left_5)


class TestBinarySearchFirst(TestCase):
    def test_correct(self):
        fp = FindPrefixes(['aa', 'ab', 'aba', 'abc', 'addd'], 'ab')
        first = fp.binary_search_first()
        self.assertEqual(first, 1)

    def test_empty(self):
        with self.assertRaises(EmptyInput):
            fp = FindPrefixes([], 'ab')
            fp.binary_search_first()

    def test_one_correct(self):
        fp = FindPrefixes(['abc'], 'ab')
        first = fp.binary_search_first()
        self.assertEqual(first, 0)

    def test_one_incorrect(self):
        with self.assertRaises(EmptyInput):
            fp = FindPrefixes(['bbbb'], 'ab')
            fp.binary_search_first()

    def test_all_correct(self):
        fp = FindPrefixes(['aba', 'abc', 'abd'], 'ab')
        first = fp.binary_search_first()
        self.assertEqual(first, 0)

    def test_all_incorrect(self):
        with self.assertRaises(EmptyInput):
            fp = FindPrefixes(['baba', 'babc', 'babd'], 'ab')
            fp.binary_search_first()

    def test_correct_pre_last_element(self):
        fp = FindPrefixes(['aaa', 'aaaaaa', 'abc', 'zzzzz'], 'ab')
        first = fp.binary_search_first()
        self.assertEqual(first, 2)

    def test_correct_last_element(self):
        fp = FindPrefixes(['aaa', 'aaaaaa', 'abc'], 'ab')
        first = fp.binary_search_first()
        self.assertEqual(first, 2)

    def test_correct_second_element(self):
        fp = FindPrefixes(['aaa', 'abc', 'adddd', 'adddd', 'zzzzz'], 'ab')
        first = fp.binary_search_first()
        self.assertEqual(first, 1)

    def test_correct_first_element(self):
        fp = FindPrefixes(['abc', 'adddd', 'adddd', 'zzzzz'], 'ab')
        first = fp.binary_search_first()
        self.assertEqual(first, 0)

    def test_correct_last_two_elements(self):
        fp = FindPrefixes(['aaaa', 'aaaab', 'aba', 'abc'], 'ab')
        first = fp.binary_search_first()
        self.assertEqual(first, 2)

    def test_correct_first_two_elements(self):
        fp = FindPrefixes(['abc', 'abz', 'dddd', 'zzzzz'], 'ab')
        first = fp.binary_search_first()
        self.assertEqual(first, 0)


class TestBinarySearchLast(TestCase):
    def test_correct(self):
        fp = FindPrefixes(['aa', 'ab', 'aba', 'abc', 'addd'], 'ab')
        first = fp.binary_search_last()
        self.assertEqual(first, 3)

    def test_empty(self):
        with self.assertRaises(EmptyInput):
            fp = FindPrefixes([], 'ab')
            fp.binary_search_last()

    def test_one_correct(self):
        fp = FindPrefixes(['abc'], 'ab')
        first = fp.binary_search_last()
        self.assertEqual(first, 0)

    def test_one_incorrect(self):
        with self.assertRaises(EmptyInput):
            fp = FindPrefixes(['bbbb'], 'ab')
            fp.binary_search_last()

    def test_all_correct(self):
        fp = FindPrefixes(['aba', 'abc', 'abd'], 'ab')
        first = fp.binary_search_last()
        self.assertEqual(first, 2)

    def test_all_incorrect(self):
        with self.assertRaises(EmptyInput):
            fp = FindPrefixes(['baba', 'babc', 'babd'], 'ab')
            fp.binary_search_last()

    def test_correct_pre_last_element(self):
        fp = FindPrefixes(['aaa', 'aaaaaa', 'abc', 'zzzzz'], 'ab')
        first = fp.binary_search_last()
        self.assertEqual(first, 2)

    def test_correct_last_element(self):
        fp = FindPrefixes(['aaa', 'aaaaaa', 'abc'], 'ab')
        first = fp.binary_search_last()
        self.assertEqual(first, 2)

    def test_correct_second_element(self):
        fp = FindPrefixes(['aaa', 'abc', 'adddd', 'adddd', 'zzzzz'], 'ab')
        first = fp.binary_search_last()
        self.assertEqual(first, 1)

    def test_correct_first_element(self):
        fp = FindPrefixes(['abc', 'adddd', 'adddd', 'zzzzz'], 'ab')
        first = fp.binary_search_last()
        self.assertEqual(first, 0)

    def test_correct_last_two_elements(self):
        fp = FindPrefixes(['aaaa', 'aaaab', 'aba', 'abc'], 'ab')
        first = fp.binary_search_last()
        self.assertEqual(first, 3)

    def test_correct_first_two_elements(self):
        fp = FindPrefixes(['abc', 'abz', 'dddd', 'zzzzz'], 'ab')
        first = fp.binary_search_last()
        self.assertEqual(first, 1)


class TestAnswer(TestCase):
    def test_correct(self):
        fp = FindPrefixes(['aa', 'ab', 'aba', 'abc', 'addd'], 'ab')
        self.assertEqual(fp.answer, ['ab', 'aba', 'abc'])

    def test_empty(self):
        fp = FindPrefixes([], 'ab')
        self.assertEqual(fp.answer, 'Sorry empty input or cannot find match')

    def test_one_correct(self):
        fp = FindPrefixes(['abc'], 'ab')
        self.assertEqual(fp.answer, ['abc'])

    def test_one_incorrect(self):
        fp = FindPrefixes(['bbbb'], 'ab')
        self.assertEqual(fp.answer, 'Sorry empty input or cannot find match')

    def test_all_correct(self):
        fp = FindPrefixes(['aba', 'abc', 'abd'], 'ab')
        self.assertEqual(fp.answer, ['aba', 'abc', 'abd'])

    def test_all_incorrect(self):
        fp = FindPrefixes(['baba', 'babc', 'babd'], 'ab')
        self.assertEqual(fp.answer, 'Sorry empty input or cannot find match')

    def test_correct_pre_last_element(self):
        fp = FindPrefixes(['aaa', 'aaaaaa', 'abc', 'zzzzz'], 'ab')
        self.assertEqual(fp.answer, ['abc'])

    def test_correct_last_element(self):
        fp = FindPrefixes(['aaa', 'aaaaaa', 'abc'], 'ab')
        self.assertEqual(fp.answer, ['abc'])

    def test_correct_second_element(self):
        fp = FindPrefixes(['aaa', 'abc', 'adddd', 'adddd', 'zzzzz'], 'ab')
        self.assertEqual(fp.answer, ['abc'])

    def test_correct_first_element(self):
        fp = FindPrefixes(['abc', 'adddd', 'adddd', 'zzzzz'], 'ab')
        self.assertEqual(fp.answer, ['abc'])

    def test_correct_last_two_elements(self):
        fp = FindPrefixes(['aaaa', 'aaaab', 'aba', 'abc'], 'ab')
        self.assertEqual(fp.answer, ['aba', 'abc'])

    def test_correct_first_two_elements(self):
        fp = FindPrefixes(['abc', 'abz', 'dddd', 'zzzzz'], 'ab')
        self.assertEqual(fp.answer, ['abc', 'abz'])
