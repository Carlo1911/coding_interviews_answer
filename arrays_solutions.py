from common import INT_MAX, INT_MIN

class ArraySolver(object):

    @staticmethod
    def find_missing_number(unordered_list, n_elements):
        """
        find missing number in array of size n containing numbers from 1 to n only.
        :param unordered_list: integer list from 1 to n (with missing element)
        :param n_elements: number of elements including the missing element
        :return:
        """
        expected_sum = n_elements * ((n_elements + 1) / 2)
        actual_sum = 0
        for item in unordered_list:
            actual_sum += item

        return expected_sum - actual_sum

    @staticmethod
    def remove_duplicate_from_list(duplicated_list):
        return list(set(duplicated_list))
    
    @staticmethod
    def get_duplicated_from_list(duplicated_list):
        """
        find all repeated numbers in list
        :param duplicated_list: unsorted integer list
        :return: list with duplicated items
        """
        return [item for item in set(duplicated_list) if duplicated_list.count(item) > 1]

    @staticmethod
    def get_largest_smallest_number(unsorted_list):
        largest = INT_MIN
        smallest = INT_MAX
        for item in unsorted_list:
            if item > largest:
                largest = item
            elif item < smallest:
                smallest = item
        return largest, smallest

    @staticmethod
    def get_pair_of_sum_n_2(unsorted_list, objective_sum):
        pairs = []
        for i in range(len(unsorted_list)):
            first = unsorted_list[i]
            for j in range(len(unsorted_list)):
                second = unsorted_list[j]
                if first + second == objective_sum:
                    pairs.append((first, second))
        return list(set(pairs))

    @staticmethod
    def get_pair_of_sum_n(unsorted_list, objective_sum):
        values_set = set(unsorted_list)
        pairs = [(item, objective_sum - item) for item in unsorted_list if (objective_sum - item) in values_set]
        return list(set(pairs))

    @staticmethod
    def get_pair_of_sum_wo_repeated(unsorted_list, objective_sum):
        unsorted_list.sort()
        pairs = []
        left_index = 0
        right_index = len(unsorted_list) - 1
        while left_index < right_index:
            actual_sum = unsorted_list[left_index] + unsorted_list[right_index]
            if actual_sum == objective_sum:
                pairs.append((unsorted_list[left_index], unsorted_list[right_index]))
                left_index += 1
                right_index -= 1
            elif actual_sum < objective_sum:
                left_index += 1
            else:
                right_index -= 1
        return pairs

