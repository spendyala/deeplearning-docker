def subset_sum(in_list, target, start, end):
    if target == 0:
        return '{0},{1}'.format(start, end-1)
    if target < 0 or end == len(in_list):
        return '-1,-1'
    target -= in_list[end]
    return subset_sum(in_list, target, start, end+1)


def solution(l, t):
    # Your code here
    for i, each_num in enumerate(l):
        ret = subset_sum(l, t, i, i)
        if ret != '-1,-1':
           return ret
    return '-1,-1'
   

print(solution([4, 3, 10, 2, 8], 12))
print(solution([1, 2, 3, 4], 15))
