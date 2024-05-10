def find_second_largest(nums: list[int]) -> int:
    if len(nums) < 2:
        raise ValueError("Not enough numbers to get the second-largest")

    nums_distinct = list(set(nums))

    if len(nums_distinct) < 2:
        return nums_distinct[0]

    second_largest = sorted(nums_distinct)[-2]
    return second_largest


def test_find_second_largest():
    assert find_second_largest([4, 2, 5, 1]) == 4
    assert find_second_largest([12, 35, 1, 10, 34, 1]) == 34
    assert find_second_largest([-2, -8, -10, -1, -100]) == -2
    assert find_second_largest([10, 10, 10]) == 10
