def get_numbers():
    return [1, 2, 3]
nums = get_numbers()
print(nums)

def get_numbers():
    yield 1
    yield 2
    yield 3

nums = get_numbers()
for num in nums:
    print(num)