def get_chunks(start, value):
    for each in range(start, 2000000001, value):
        yield range(each, each+value)

def sum_xor_n(value):
    mod_value = value&3
    if mod_value == 3:
        return 0
    elif mod_value == 2:
        return value+1
    elif mod_value == 1:
        return 1
    elif mod_value == 0:
        return value
    else:
        return None

def get_numbers_xor(start, end):
    start_xor = sum_xor_n(start-1)
    end_xor = sum_xor_n(end)
    return start_xor^end_xor

def solution(start, length):
    # Your code here
    checkpoint = length-1
    value = 0
    for each_chunk in get_chunks(start, length):
        if checkpoint < 0:
            break
        temp = get_numbers_xor(
            each_chunk[0],
            each_chunk[checkpoint])
        if checkpoint == 0:
            value ^= each_chunk[0]
        else:
            value ^= temp
        checkpoint -= 1
    return value

print(solution(0, 3))
print(solution(17, 4))
