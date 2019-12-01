N = int(input())
As = list(map(int, input().split(" ")))

IDs = range(1, len(As)+1)
result_dict = dict(zip(IDs,As))
result_dict = sorted(result_dict.items(), key=lambda x:x[1])
result_list = list(map(lambda x: str(x[0]), result_dict))
result = " ".join(result_list)
print(result)
