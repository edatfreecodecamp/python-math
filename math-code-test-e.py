# Tests for Foundational Math Cert 5

def step00():
    print("Code test passed")
    print("Go on to the next step")


def step01():
    print("Was your prediction correct? What is the next number in the sequence?")
    print("Code test passed")
    print("Go on to the next step")


def step02(code):
    import re
    print(" ")
    # print(3+2*a, ", ", end=" ")
    if re.search("print\(3\s*\+\s*2\*a\,\s*\"\,\s*\"\,\s*end\=\"\s*\"\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use print(3+2*a, \", \", end=\" \") in your code")


def step03(code):
    import re
    print(" ")
    # print(3*2**a, ", ", end=" ")
    if re.search("print\(3\*2\*\*a\,\s*\"\,\s*\"\,\s*end\=\"\s*\"\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use print(3*2**a, \", \", end=\" \") in your code")


def step04(code):
    import re
    print(" ")
    code_count = 0
    # next_number = a_list[n-1]*2+3
    if re.search("next\_number\s*=\s*0", code):
        print("Now just change the \'next_number = 0\' line")
    elif re.search("next\_number\s*=\s*a\_list\[n\-1\]\*2\+3", code):
        print("Code test passed")
    else:
        print("You should use next_number = a_list[n-1]*2+3 in your code")


def step05(code):
    import re
    print(" ")
    # fib[n-1] + fib[n-2]
    if re.search("fib\[n\-1\]\s*\+\s*fib\[n\-2\]", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use fib[n-1] + fib[n-2] in your code")


def step06(code):
    import re
    print(" ")
    code_count = 0
    # for x in range(len(b_list)):
    if re.search("range\(len\(b\_list\)\)\:", code):
        code_count = code_count + 1
    else:
        print("You should use range(len(b_list)): in your code")

    # plt.plot([x], [b_list[x]], 'bo')
    if re.search("plt\.plot\(\[[a-z]\]\,\s*\[b\_list\[[a-z]\]\]\,", code):
        code_count = code_count + 1
    else:
        print("You should use plt.plot([n], [b_list[n]], \'ro\') in your code")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step07(code):
    import re
    print(" ")
    # sum = sum + element
    if sum==0:
        print("Now update the sum variable in the loop")
    elif re.search("sum\s*\=\s*sum\s*\+\s*element", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use sum = sum + element in your code")


def step08(code):
    import re
    print(" ")
    if re.search("range\(11\)\:", code):
        print("Now change the range to 42 and run this again")
    elif re.search("range\(42\)\:", code):
        print("Now change the range to 100 and run this again")
    if re.search("range\(100\)\:", code):
        print("Code test passed")
        print("Go on to the next step")


def step09(code):
    import re
    print(" ")
    # print(math.factorial(number),
    if re.search("print\(number\,\s*\"\!\s*\=\s*\"\)", code):
        print("Now change the first print statement to include math.factorial()")
    elif re.search("print\(number\,\s*\"\!\s*\=\s*\"\,math\.factorial\(number\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use print(number, \"! = \", math.factorial(number)) in your code")


def step10(code):
    import re
    print(" ")
    # for a in range(11):
    if re.search("for a in range\(11\)\:", code):
        print("Now change the range to be 100")
    elif re.search("for a in range\(100\)\:", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use for a in range(100): in your code")


def step11(code):
    import re
    print(" ")
    # probability = correct/possible
    if re.search("probability\s*\=\s*correct\/possible", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use probability = correct/possible in your code")


def step12(code):
    import re
    print(" ")
    if re.search("combined\_prob\s*\=\s*0", code):
        print("Now change the combined_prob line")
    elif re.search("combined\_prob\s*\=\s*prob\*prob\*prob\*prob", code):
        print("Code test passed")
        print("Go on to the next step")
    elif re.search("combined\_prob\s*\=\s*prob\*\*4", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use combined_prob = prob**4 in your code")


def step13(code):
    import re
    print(" ")
    if re.search("combined\_prob\s*\=\s*0", code):
        print("Now change the combined_prob line")
    elif re.search("combined\_prob\s*\=\s*prob\s*\+\s*prob\s*\+\s*prob", code):
        print("Code test passed")
        print("Go on to the next step")
    elif re.search("combined\_prob\s*\=\s*prob\s*\*3", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use combined_prob = prob + prob + prob in your code")


def step14(code):
    import re
    print(" ")
    # starters = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    if re.search("starters\s*\=\s*0", code):
        print("Now change the starters = 0 line")
    elif re.search("starters\s*\=\s*math\.factorial\(n\)\/\(math\.factorial\(r\)\*math\.factorial\(n\s*\-\s*r\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use starters = math.factorial(n)/(math.factorial(r)*math.factorial(n-r)) in your code")

def step15(code):
    import re
    print(" ")
    # arr = math.factorial(n)/math.factorial(n-r)
    if re.search("arr\s*\=\s*0", code):
        print("Now change the arr = 0 line")
    elif re.search("arr\s*\=\s*math\.factorial\(n\)\/math\.factorial\(n\s*\-\s*r\)", code):
        print("Code test passed")
    else:
        print("You should use arr = math.factorial(n)/math.factorial(n-r) in your code")

