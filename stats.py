def mean(nums):
    # takes in a list of numbers
    # returns the mean or sum
    return sum(nums) / len(nums)


def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return sorted(lst)[n // 2]
    return mean(sorted(lst)[n // 2 - 1:n // 2 + 1])


def variance(lst):
    return mean([(n - mean(lst))**2 for n in lst])
