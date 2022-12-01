import copy

# 利用回溯法求解皇后问题。

# k 行数
# n n皇后问题
# queen 皇后位置
# attack 攻击坐标组
# solve 存储N皇后

def put(attack,k:int,c:int,n:int):
    col = c
    row = k
 #   print('('+str(k)+','+str(c)+')')
    if attack[row][col] == False:
        return False
    # 行
    for tmp_col in range(n):
        attack[row][tmp_col] = False
    # 列
    for tmp_row in range(n):
        attack[tmp_row][col] = False
    # 斜1
    for i in range(1,min(n-col-1,row)+1):
        attack[row-i][col+i] = False # ↗️
    for i in range(1,min(col,n-row-1)+1):
        attack[row+i][col-i] = False # ↙️
    # 斜-1
    for i in range(1,min(col,row)+1):
        attack[row-i][col-i] = False # ↖️
    for i in range(1,min(n-col-1,n-row-1)+1):
        attack[row+i][col+i] = False # ↘️
    return True
def backtrack(k:int,n:int,queen,attack,solve):
    if k==n:
        item_queen = copy.deepcopy(queen)
        solve.append(item_queen)
        return
    for i in range(n):
        tmp_attack = copy.deepcopy(attack)
        if put(attack,k,i,n):
            tmp_queen = copy.deepcopy(queen)
            queen[k][i]='Q'
            backtrack(k+1,n,queen,attack,solve)
            queen = copy.deepcopy(tmp_queen)
            attack = copy.deepcopy(tmp_attack)
        



if __name__ == '__main__':
    # n = input('请输入N皇后问题的N：')
    n=8
    queen = [['.' for _ in range(n)]for j in range(n)]
    attack = [[True for _ in range(n)]for j in range(n)]
    solve = []
    backtrack(0,n,queen,attack,solve)
    i = 0
    #for queen in solve:
    #    i = i+1
    #    print('第%s种解法：'%i)
    #    for row in queen:
    #        print(row)
    print('共有%d种解法'%len(solve))