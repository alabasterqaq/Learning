def b_search(a, target):
    left, right = 0, len(a) - 1
    while left <=right:
        mid = (left + right)//2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1

a = [4, 5, 8, 9, 12]
target = 9
res = b_search(a, target)

if res != -1:
    print(f'目标元素{target}在列表中的索引为{res}')
else:
    print('不在')