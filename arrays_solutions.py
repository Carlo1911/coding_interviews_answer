
class ArraySolver(object):
    def find_missing_number(self, unordered_list, n_elements):
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

    def remove_duplicate_from_list(self, duplicated_list):
        return list(set(duplicated_list))

    def get_duplicated_from_list(self, duplicated_list):
        return [item for item in set(duplicated_list) if duplicated_list.count(item) > 1]
