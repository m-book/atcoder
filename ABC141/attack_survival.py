n_k_q_str = input()
n_k_q = n_k_q_str.split(" ")
N = int(n_k_q[0])
K = int(n_k_q[1])
Q = int(n_k_q[2])
answers = [0] * N
for i in range(Q):
    answer = int(input()) - 1
    answers[answer] += 1

for i in range(N):
    if K - (Q - answers[i]) > 0:
        print("Yes")
    else:
        print("No")