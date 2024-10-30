import random

def partition(arr, left, right):
    pivot_value = arr[left]
    low = left + 1
    high = right

    while True:
        while low <= high and arr[high] >= pivot_value:
            high -= 1
        while low <= high and arr[low] <= pivot_value:
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[left], arr[high] = arr[high], arr[left]
    return high

def randomized_select(arr, left, right, k):
    if left == right:  # 只有一个元素
        return arr[left]

    # 随机选择一个基准元素
    pivot_index = random.randint(left, right)
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]  # 移动基准到左边
    pivot_index = partition(arr, left, right)

    # 找到基准元素的位置
    j = pivot_index - left + 1
    if k == j:  # 找到第 k 小的元素
        return arr[pivot_index]
    elif k < j:
        return randomized_select(arr, left, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, right, k - j)

# 使用示例
array = [3, 1, 2, 5, 4, 6]
k = 3  # 查找第 3 小的元素
result = randomized_select(array, 0, len(array) - 1, k)
print(f'第 {k} 小的元素是: {result}')
