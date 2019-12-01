from numpy.linalg import solve
# from scipy.special import comb

goal = list(map(lambda x: int(x), input().split(" ")))


def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


x = goal[0]
y = goal[1]

left = [[1, 2],
        [2, 1]]

right = [x, y]

# print(solve(left, right))

result = solve(left, right)
if result[0].is_integer() is False or result[1].is_integer() is False:
    print(0)
else:
    a = (int(result[0]))
    b = (int(result[1]))

    print(cmb(a+b, a, mod))
