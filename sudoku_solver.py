from pulp import *


def sudoku_solver(input_data):
    # 数字，行，列的范围都是1-9
    VALS = ROWS = COLS = range(1, 10)

    # 构造3*3的小方格
    Boxes = [
        [(3 * i + k + 1, 3 * j + l + 1) for k in range(3) for l in range(3)]
        for i in range(3)
        for j in range(3)
    ]

    # 建立问题
    prob = LpProblem("Sudoku Problem")

    # 建立决策变量
    choices = LpVariable.dicts("X", (VALS, ROWS, COLS), cat="Binary")

    # 约束：每个格子只能填入一个数字
    for r in ROWS:
        for c in COLS:
            prob += lpSum([choices[v][r][c] for v in VALS]) == 1

    # 约束：每行、每列、每个3*3小方格1-9不重复
    for v in VALS:
        for r in ROWS:
            prob += lpSum([choices[v][r][c] for c in COLS]) == 1
        for c in COLS:
            prob += lpSum([choices[v][r][c] for r in ROWS]) == 1
        for b in Boxes:
            prob += lpSum([choices[v][r][c] for (r, c) in b]) == 1

    # 约束：初始状态填入的数字
    for (v, r, c) in input_data:
        prob += choices[v][r][c] == 1

    # 求解
    prob.solve()

    # 存储是否有解的状态
    status = LpStatus[prob.status]  # Infeasible  Optimal

    if status == 'Infeasible':
        return status, []

    # 存储结果为三元组列表
    res = []
    for r in ROWS:
        for c in COLS:
            for v in VALS:
                if value(choices[v][r][c]) == 1:
                    res.append((v, r, c))
    return status, res
