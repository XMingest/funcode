# -*- coding: utf-8 -*-

# 包含四则运算、小括号的表达式，如：4+2，或((((2+3)*2+4.02)*4)+2)*4
# 输入包含多组数据，当一行中只有0时输入结束，相应的结果不要输出

valid_op = {
    '#': {'lv': -1},
    '+': {'lv': 0, '_': lambda a, b: a + b},
    '-': {'lv': 0, '_': lambda a, b: a - b},
    '*': {'lv': 1, '_': lambda a, b: a * b},
    '/': {'lv': 1, '_': lambda a, b: a / b},
}

def calculate_noparentheses(expression: str):
    nums = []
    ops = []
    last_num = ''
    for ei in expression + '#':
        if not last_num and ei == '-':
            last_num += '-'
        elif ei in valid_op:
            last_num = float(last_num)
            while ops and valid_op[ops[-1]]['lv'] >= valid_op[ei]['lv']:
                op = ops.pop()
                last_num = valid_op[op]['_'](nums.pop(), float(last_num))
            nums.append(last_num)
            ops.append(ei)
            last_num = ''
        else:
            last_num += ei
    return nums.pop()

def calculate(expression: str):
    while True:
        start = 0
        end = 0
        for i in range(len(expression)):
            if expression[i] == '(':
                start = i
            elif expression[i] == ')':
                end = i
                break
        else:
            return calculate_noparentheses(expression)
        expression = expression[: start] + str(calculate_noparentheses(expression[start + 1: end])) + expression[end + 1:]

if __name__ == "__main__":
    while True:
        instr = input()
        if instr == '0':
            break
        result = calculate(instr)
        print('%.2f' % result)
