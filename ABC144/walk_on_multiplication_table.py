def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

num = int(input())

divisors = make_divisors(num)

min = float('inf')

for n in reversed(divisors):
    temp = num / n
    temp_result = (n-1) + (temp-1)
    if temp_result < min:
        min = temp_result

print(int(min))
