def matrix_chain_order(p):
    n = len(p) - 1  # 矩阵数量
    # m[i][j] 存储从第 i 个矩阵到第 j 个矩阵的最小乘法次数
    m = [[0] * n for _ in range(n)]
    # s[i][j] 存储最佳分割点
    s = [[0] * n for _ in range(n)]

    # l 是链的长度
    for l in range(2, n + 1):  # l 从2到n
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')  # 初始化为无穷大
            for k in range(i, j):  # k 是分割点
                # 计算乘法次数
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:  # 找到更小的乘法次数
                    m[i][j] = q
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")


# 示例用法
p = [30, 35, 15, 5, 10, 20, 25]  # 矩阵维度数组
m, s = matrix_chain_order(p)

print("最小乘法次数:", m[0][len(p) - 2])
print("最佳矩阵乘法顺序:", end=" ")
print_optimal_parens(s, 0, len(p) - 2)
print()
