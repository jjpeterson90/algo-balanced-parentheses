import re

def balance_parens(str):
    tracker = [[],[]] # tracker[0] logs parens, tracker[1] logs indexes of open parens
    str = list(char for char in str)
    result = ''
    for i in range(len(str)):
        if str[i] == '(':
            tracker[0].append(str[i])
            tracker[1].append(i)
        elif str[i] == ')':
            if len(tracker[0]) == 0:
                str[i] = ''
            elif tracker[0][-1] == '(':
                tracker[0].pop()
                tracker[1].pop()
    if len(tracker[1]) != 0:
        for saved_index in tracker[1]:
            str[saved_index] = ''
    for char in str:
        result += char
    return result
            
# () () ) () )   >>   () () ()
# print(balance_parens("abc(d)e(fgh))(i)j)k"))# == "abc(d)e(fgh)(i)jk")

# # ( () () () (   >>   () () ()
# print(balance_parens("abc((d)e(fgh)(i)j(k"))# == "abc(d)e(fgh)(i)jk")

# # () ( ( () ) ) ) () )   >>   () ( ( () ) ) ()
# print(balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p"))# == "abc(d)(ef(g(h))ij)klm()op")