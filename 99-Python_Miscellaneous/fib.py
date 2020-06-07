# Fib
# 5
#     0
#     1
# 0+1=1
# 1+1=2
# 2+1=3
# 3+2=5
# 5+3=8
# 8+5=13
#
#
# f(n) = f(n-1)+f(n-2)
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1)+fib(n-2)
#     # n >=2
# print(fib(0))
#
# print(fib(7))
# 0!=1
# 1!=1 * 0!
# 2!=2
# 3!=6
# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

import json
with open('some.json') as f_obj:
    f_data = f_obj.read()

file_json_data = json.loads(f_data)

def json_parser(json_obj, key, second_key):
    if not isinstance(json_obj, dict):
        return None
    if key in json_obj:
        return json_obj.get(key)
    for each_key in json_obj.keys():
        tracking = []
        val = json_parser(json_obj.get(each_key), key, second_key)
        if val:
            tracking.append((each_key, val))
        for each_in_track in tracking:
            if each_in_track[0] == second_key:
                return each_in_track[1]


print(json_parser(file_json_data, 'state'))
