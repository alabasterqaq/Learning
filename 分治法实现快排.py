def q(arr):
    if len(arr) <= 1:
        return arr
    standard = arr[-1]
    left = []
    right = []
    for element in arr[:-1]:
        if element < standard:
            left.append(element)
        else:
            right.append(element)
    return q(left) + [standard] + q(right)#此处进行递归调用

arr = [33, 34, 11, 87, 3, 9]
end = q(arr)
print(f'排序后的数组为{end}')
