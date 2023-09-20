import random

'''
1658 - Minimum Operations to Reduce X to Zero
'''
def generate() -> str:
    tests = []
    min_num = 1
    max_num = int(1e5)
    minval = 1
    maxval = int(1e4)

    nums = [random.randint(minval, maxval)]
    x = sum(nums) - 1
    tests.append(nums.__str__().replace(' ', '') + "\n" + str(x))

    nums = [random.randint(minval, maxval)]
    x = sum(nums) + 1
    tests.append(nums.__str__().replace(' ', '') + "\n" + str(x))

    nums = [random.randint(minval, maxval)]
    x = sum(nums)
    tests.append(nums.__str__().replace(' ', '') + "\n" + str(x))

    nums = [1 for _ in range(max_num)]
    x = sum(nums)
    tests.append(nums.__str__().replace(' ', '') + "\n" + str(x))

    for l in range(7, 0, -2):
        nums = [random.randint(minval, maxval) for _ in range(max_num // l)]
        x = min(sum(nums), 10**9)
        tests.append(nums.__str__().replace(' ', '') + "\n" + str(x))

    return '''
'''.join(tests)
