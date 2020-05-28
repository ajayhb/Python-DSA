class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)
        return True

    def pop(self):
        if len(self.items) == 0:
            return -1
        else:
            data = self.items.pop()
            return data

def check_balanced_paranthesis(input_arr):
    """Check if paranthesis are balanced or not"""
    input_arr = [char for char in input_arr]
    if len(input_arr) == 0:
        print("Empty array")

    elif len(input_arr) % 2 != 0:
        print("Input length must be an even number")

    else:
        matching_paranthesis = set([('{', '}'), ('[', ']'), ('(', ')')])
        opening_brackets = set('({[')
        matched = True
        stack = Stack()
        
        for i in input_arr:
            if i in opening_brackets:
                stack.push(i)
            else:
                data = stack.pop()
                if data == -1:
                    matched = False
                    break
                else:
                    compare_set = (f'{data}', f'{i}')
                    if compare_set not in matching_paranthesis:
                        matched = False
                        break

        if stack.isEmpty() and matched == True:
            print("Paranthesis Matched")
        else:
            print("Paranthesis Not Matched")

if __name__ == '__main__':
    check_balanced_paranthesis("{{{[[(()())]]}}}()")
    check_balanced_paranthesis("({{{[[(())]]}}})")

    check_balanced_paranthesis("({{{}}}(")
    check_balanced_paranthesis("({{{[[(())")

    check_balanced_paranthesis("")
    check_balanced_paranthesis("({{{[[()())]]}}})")
