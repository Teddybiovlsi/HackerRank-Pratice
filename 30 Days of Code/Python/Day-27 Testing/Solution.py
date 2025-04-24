# HackerRank - 30 Days of Code: Day 27 - Testing
# Problem: https://www.hackerrank.com/challenges/30-testing/problem
#
# Objective:
# Write unit tests for a function that finds the index of the minimum value in an array.
# Includes handling of edge cases:
# - Empty array (raise ValueError)
# - Unique values
# - Exactly two identical minimums (must return first one)

# ---- Function Under Test ----

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

# ---- Test Data Providers ----

class TestDataEmptyArray:
    @staticmethod
    def get_array():
        # Returns an empty array (should raise ValueError)
        return []

class TestDataUniqueValues:
    @staticmethod
    def get_array():
        # Returns a list of unique integers
        return [3, 1, 4, 7]

    @staticmethod
    def get_expected_result():
        # The index of the minimum value (1) is 1
        return 1

class TestDataExactlyTwoDifferentMinimums:
    @staticmethod
    def get_array():
        # Returns an array with exactly two minimum values
        return [4, 2, 3, 2, 5]

    @staticmethod
    def get_expected_result():
        # Index of the first occurrence of the minimum (2)
        return 1

# ---- Unit Test Functions ----

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError:
        pass  # Passed test
    else:
        assert False, "Expected ValueError was not raised"

def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2
    assert len(set(seq)) == len(seq)  # Ensure all values are unique

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result, "Result does not match expected index"

def TestWithExactlyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    assert sorted(seq).count(min(seq)) == 2  # Ensure exactly 2 minimums

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result, "Did not return index of first minimum"

# ---- Run All Tests ----

TestWithEmptyArray()
TestWithUniqueValues()
TestWithExactlyTwoDifferentMinimums()
print("All tests passed.")
