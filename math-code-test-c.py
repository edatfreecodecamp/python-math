# Tests for Foundational Math Cert 3


def step00():
    print("Code test passed")
    print("Go on to the next step")


def step01(code):
    import re
    print(" ")
    if re.search("plt\.fill_between\(x\,\s*y1\,\s*0\)", code):
        print("Now change the code to shade above the line and run it again.")
    elif re.search("plt\.fill_between\(x\,\s*y1\,\s*ymax\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use plt.fill_between(x, y1, ymax) in your code")


def step02(code):
    import re
    print(" ")
    if re.search("plt\.plot\(x\,\s*y1\)", code):
        print("Now change the code to make a dashed red line and run it again.")
    elif re.search("plt\.plot\(x\,\s*y1\,\s*\'r\-\-\'\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use plt.plot(x, y1, 'r--') in your code")


def step03(code):
    import re
    print(" ")
    if re.search("\(x\,\s*y1\,\s*10\,\s*facecolor\s*\=\s*\'red\'\)", code):
        print("Now change the code to reverse the color order.")
    elif re.search("plt\.fill\_between\(x\,\s*y1\,\s*10\,\s*facecolor\=\'blue\'\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("you should use `plt.fill_between(x, y1, 10, facecolor='blue')` in your code")


def step05(code):
    import re
    print(" ")
    code_count = 0
    if re.search("c\s*\=\s*int\(input\(\"Enter coefficient C\:\s*\"\)\)", code):
        code_count = code_count + 1
    else:
        print("You should use c = int(input(\"Enter coefficient C: \")) in your code")

    if re.search("d\s*\=\s*int\(input\(\"Enter coefficient D\:\s*\"\)\)", code):
        code_count = code_count + 1
    else:
        print("You should use d = int(input(\"Enter coefficient D: \")) in your code")

    if re.search("y\s*\=\s*a\*x\*\*3\s*\+\s*b\*x\*\*2\s*\+\s*c\*x\s*\+\s*d", code):
        code_count = code_count + 1
    else:
        print("You should use y = a*x**3 + b*x**2 + c*x + d in your code")

    if code_count==3:
        print("Code test passed")
        print("Go on to the next step")


def step06(code):
    import re
    print(" ")
    code_count = 0
    if re.search("plt\.plot\(x\,\s*a\*x\*\*2\s*\+\s*b\*x\)", code):
        print("Now change the three lines of code and run this again.")
    elif re.search("plt\.plot\(x\,\s*a\*x\*\*2\s*\+\s*b\*x\s*\+\s*c\)", code):
        code_count = code_count + 1

    if re.search("f\(a\,\s*b\,\s*c\)", code):
        code_count = code_count + 1

    if re.search("c\s*=\s*\(\-9\,\s*9\)\)", code):
        code_count = code_count + 1

    if code_count==3:
        print("Code test passed")
        print("Go on to the next step")


def step07(code):
    import re
    print(" ")
    code_count = 0
    if re.search("a\s*=\s*\(1\,\s*9\)\,\s*b\=\(1\,\s*9\)\)", code):
        print("Now change the interactive_plot and run this again.")
    elif re.search("a\s*=\s*\(\-9\,\s*\-1\)\,\s*b\=\(1\,\s*9\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use interactive(f, a=(-9, -1), b=(1, 9)) in your code.")


def step08(code):
    import re
    print(" ")
    if re.search("a\s*\=\s*p\*\(1\s*\+\s*r\)\*\*t", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use a = p*(1+r)**t in your code.")


def step09(code):
    import re
    print(" ")
    if re.search("a\s*\=\s*p\*\(1\s*\-\s*r\)\*\*t", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use a = p*(1-r)**t in your code.")


def step10(code):
    import re
    print(" ")
    if re.search("annuity\s*\=\s*p\*\(1\s*\+\s*\(r\/n\)\)\*\*\(n\*t\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use annuity = p*(1+(r/n))**(n*t) in your code.")


def step11(code):
    import re
    print(" ")
    code_count = 0
    # a_annual = p*(1+r)**t
    if re.search("a\_annual\s*\=\s*p\*\(1\+r\)\*\*t", code):
        code_count = code_count + 1
    else:
        print("You should use a_annual = p*(1+r)**t in your code")

    # a_n_times = p*(1+r/n)**(n*t)
    if re.search("a\_n\_times\s*\=\s*p\*\(1\+r\/n\)\*\*\(n\*t\)", code):
        code_count = code_count + 1
    else:
        print("You should use a_n_times = p*(1+r/n)**(n*t) in your code")

    # a_continuous = p*math.e**(r*t)
    if re.search("a\_continuous\s*\=\s*p\*math\.e\*\*\(r\*t\)", code):
        code_count = code_count + 1
    else:
        print("You should use a_continuous = p*math.e**(r*t) in your code")

    if code_count==3:
        print("Code test passed")
        print("Go on to the next step")


def step12(p,r,t,monthly,annuity):
    print(" ")
    a2 = p
    for b in range(12*t):
        a2 = a2 + monthly
        interest = a2*r/12
        a2 = a2 + interest

    if annuity==a2:
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use interest = annuity * r / 12 in your code.")


def step13(p,r,t,pmt):
# one solution:
    mult = 1+(r/12)
    exp = 12*t
    top = r/12*mult**exp
    bot = (mult**exp)-1
    pmt2 = p*top/bot
    print(" ")
    if pmt==pmt2:
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Here is one way to write the code, using extra variables:")
        print("mult = 1+r/12")
        print("exp = 12*t")
        print("top = r/12*mult**exp")
        print("bot = (mult**exp)-1")
        print("pmt = top/bot")


def step14(code):
    import re
    print(" ")
    if re.search("exp\s*\=\s*math\.log\(result\,\s*base\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use exp = math.log(result, base) in your code")


# Step 15 re-uses step00()


def step16(code):
    import re
    print(" ")
    if re.search("exp\s*\=\s*math\.floor\(math\.log\(n\,\s*10\)\)", code):
        print("Now remove the math.floor function and run it again.")
    elif re.search("exp\s*\=\s*math\.log\(n\,\s*10\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use exp = math.log(n, 10) in your code")


def step17(b1,b2):
    import re
    print(" ")
    code_count = 0
    if b1==4.13:
        code_count = code_count + 1
    else:
        print("b1 should be 4.13")

    if b2==-10:
        code_count = code_count + 1
    else:
        print("b2 should be -10")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step18(code):
    import re
    print(" ")
    code_count = 0
    if re.search("x2\s*\=\s*math\.floor\(math\.log\(b\,\s*10\)\)", code):
        code_count = code_count + 1
    else:
        print("You should use x2 = math.floor(math.log(b,10)) in your code")

    if re.search("n2\s*\=\s*round\(b\*10\*\*\(\-x2\)\,\s*2\)", code):
        code_count = code_count + 1
    else:
        print("You should use n2 = round(b*10**(-x2),2) in your code")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step19(code):
    import re
    print(" ")
    code_count = 0
    if re.search("x\s*=\s*math\.floor\(math\.log\(a\,\s*10\)\)", code):
        code_count = code_count + 1
    else:
        print("You should use x = math.floor(math.log(a,10)) in your code")

    if re.search("n\s*=\s*round\(a\*10\*\*\(\-x\)\,\s*2\)", code):
        code_count = code_count + 1
    else:
        print("You should use n = round(a*10**(-x),2) in your code")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step20(code):
    import re
    print(" ")
    code_count = 0

    # plt.plot(x2, np.log2(x2), 'g')
    if re.search("plt\.plot\(x1\,\s*math\.e\*\*x1\,\s*\'b\'\)", code):
        print("Now change the blue line and run this again")
    elif re.search("plt\.plot\(x2\,\s*np\.log2\(x2\)\,\s*\'g\'\)", code):
        code_count = code_count + 1
    else:
        print("You should use plt.plot(x2, np.log2(x2), 'g') in your code")

    # plt.plot(x1, 2**x1, 'b')
    if re.search("plt\.plot\(x1\,\s*math\.e\*\*x1\,\s*\'b\'\)", code):
        print("Now change the green line and run this again")
    elif re.search("plt\.plot\(x1\,\s*2\*\*x1\,\s*\'b\'\)", code):
        code_count = code_count + 1
    else:
        print("You should use plt.plot(x1, 2**x1, 'b') in your code")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step21(code):
    # math.ceil(-math.log(decimal, 10))
    import re
    print(" ")
    if re.search("math\.ceil\(\-math\.log\(decimal\,\s*10\)\)", code):
        print("Code test passed")
    else:
        print("You should use h = math.ceil(-math.log(decimal, 10)) in your code")













