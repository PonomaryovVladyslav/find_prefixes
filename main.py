""" File with solution"""
from random import choice
from functools import wraps
import time


def timeit(func):
    """
    decorator to calc time to execute function
    :param func: function which will be run
    :return: func
    """

    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        """
        execution of function with time calculation
        :param args: func args
        :param kwargs: func kwargs
        :return: result of function
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Took {total_time:.4f} seconds')
        return result

    return timeit_wrapper


class EmptyInput(Exception):
    """except if input is empty"""


class FindPrefixes:
    """
    class to calculate strings which starts from prefix with using binary search
    """

    def __init__(self, input_list, prefix=''):
        """
        initialization
        :param input_list: sorted list of strings
        :param prefix: string
        """
        self.input_list = input_list
        self.prefix = prefix

    def get_end_and_mid(self, start, end):
        """
        calculate mid and end elements in recursion
        :param start: number
        :param end: number or None
        :return: tuple with 2 numbers
        """
        end = len(self.input_list) if not end else end
        mid = (start + end) // 2
        return end, mid

    def is_left_first(self, check):
        """
        method to check if we have to move left when try to find first element
        :param check: index of checking element
        :return: boolean
        """
        both_fit = self.input_list[check].startswith(self.prefix) and self.input_list[check + 1].startswith(
            self.prefix)
        both_more = self.input_list[check] > self.prefix and self.input_list[check + 1] > self.prefix
        first_fit_second_mode = self.input_list[check].startswith(self.prefix) and self.input_list[
            check + 1] > self.prefix
        return both_fit or both_more or first_fit_second_mode

    def is_left_last(self, check):
        """
        method to check if we have to move left when try to find last element
        :param check: index of checking element
        :return: boolean
        """
        return (not self.input_list[check - 1].startswith(self.prefix) and self.input_list[check - 1] > self.prefix) \
               and (not self.input_list[check].startswith(self.prefix) and self.input_list[check] > self.prefix)

    def binary_search_first(self, start=0, end=None):
        """
        recursion method using binary search to find first fit element
        :param start: index
        :param end: index
        :return: index of first element or raise exception
        """
        end, mid = self.get_end_and_mid(start, end)
        try:
            if not mid:
                if self.input_list[0].startswith(self.prefix):
                    return 0
                else:
                    raise EmptyInput
            elif self.input_list[mid].startswith(self.prefix) and not self.input_list[mid - 1].startswith(
                    self.prefix):
                return mid
            elif end == len(self.input_list) and mid == len(self.input_list) - 1:
                return self.binary_search_first(start=end, end=end)
            if self.is_left_first(mid):
                return self.binary_search_first(start=start, end=mid)
            else:
                return self.binary_search_first(start=mid, end=end)
        except IndexError:
            raise EmptyInput
        except EmptyInput:
            raise EmptyInput

    def binary_search_last(self, start=0, end=None):
        """
        recursion method using binary search to find last fit element
        :param start: index
        :param end: index
        :return: index of first element or raise exception
        """
        end, mid = self.get_end_and_mid(start, end)
        try:
            if not mid:
                if self.input_list[0].startswith(self.prefix):
                    return 0
                else:
                    raise EmptyInput
            elif self.input_list[mid - 1].startswith(self.prefix) and not self.input_list[mid].startswith(
                    self.prefix):
                return mid - 1
            elif end == len(self.input_list) and mid == len(self.input_list) - 1:
                return mid
            if self.is_left_last(mid):
                return self.binary_search_last(start=start, end=mid)
            else:
                return self.binary_search_last(start=mid, end=end)
        except IndexError:
            raise EmptyInput

    @property
    @timeit
    def answer(self):
        """
        property which will return answer
        :return: slice from original input
        """
        try:
            first = self.binary_search_first()
        except EmptyInput:
            return 'Sorry empty input or cannot find match'
        last = self.binary_search_last() + 1
        return self.input_list[first:last]


@timeit
def simple_way(input_list, prefix):
    """
    function to run the same logic very simple way
    :param input_list: sorted list of strings
    :param prefix: string
    :return: list with answers
    """
    return [s for s in input_list if s.startswith(prefix)]


if __name__ == '__main__':
    ascii_lowercase = 'abcde'
    sorted_random_list = sorted([''.join(choice(ascii_lowercase) for _ in range(5)) for _ in range(1000000)])
    fp = FindPrefixes(sorted_random_list, 'ab')
    # just to run method
    fp.answer
    simple_way(sorted_random_list, 'ab')
