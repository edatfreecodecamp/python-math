# Tests for Foundational Math Cert 2

def step01():
    print("Code test Passed")
    print("Go on to the next step")


def step02(code):
    import re
    print(" ")
    if re.search("plt\.axis\(\[\-20\,\s*20\,\s*\-20\,\s*20\]\)", code):
        print("Code test passed")
        print("Go on to the next step")
    elif re.search("plt\.axis\(\[\-10\,\s*10\,\s*\-10\,\s*10\]\)", code):
        print("Now change the values in plt.axis() and re-run the code.")
    else:
        print("You should use plt.axis([-20,20,-20,20]) in your code")


def step03(code):
    import re
    print(" ")
    if re.search("xmax\s*=\s*20", code):
        print("Code test passed")
        print("Go on to the next step")
    elif re.search("xmax\s*=\s*10", code):
        print("Now change the values xmax to 20 and re-run the code.")
    else:
        print("You should use xmax = 20 in your code")


def step04(code):
    import re
    print(" ")
    code_count = 0
    #plt.plot([xmin,xmax],[0,0],'b') # blue x axis
    if re.search("plt\.plot\(\[xmin\,xmax\]\,\[0\,0\]\,\s*\'g\'\)", code):
        code_count = code_count+1
    elif re.search("plt\.plot\(\[xmin\,xmax\]\,\[0\,0\]\,\s*\'b\'\)", code):
        print("Now change the 'b' to 'g' for each axis and re-run the code.")
    else:
        print("You should use plt.plot([xmin,xmax],[0,0],'g') in your code")

    #plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
    if re.search("plt\.plot\(\[0\,0\]\,\[ymin\,ymax\]\,\s*\'g\'\)", code):
        code_count = code_count+1
    elif re.search("plt\.plot\(\[0\,0\]\,\[ymin\,ymax\]\,\s*\'b\'\)", code):
        print("Now change the 'b' to 'g' for each axis and re-run the code.")
    else:
        print("You should use plt.plot([0,0],[ymin,ymax], 'g') in your code")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step05(code):
    import re
    print(" ")
    if re.search("plt\.plot\(\[\-5\]\,\s*\[1\]\,\s*\'ro\'\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use plt.plot([-5],[1], \'ro\') in your code")


def step06(code):
    import re
    code_count = 0
    print(" ")
    if re.search("x\s*\=\s*\[4\,\s*1\,\s*2\]", code):
        code_count = code_count + 1
    else:
        print("You should use x = [4,1,2] in your code")

    if re.search("y\s*\=\s*\[2\,\s*1\,\s*5\]", code):
        code_count = code_count + 1
    else:
        print("You should use y = [2,1,5] in your code")

    if code_count == 2:
        print("Code test passed")
        print("Go on to the next step")


def step07(code):
    import re
    code_count = 0
    print(" ")
    if re.search("plt.plot\(linex\,\s*liney\,\s*\'r\'\)", code):
        code_count = code_count + 1
    else:
        print("You should use plt.plot(linex, liney, \'r\') in your code")

    if re.search("plt.plot\(pointx\,\s*pointy\,\s*\'gs\'\)", code):
        code_count = code_count + 1
    else:
        print("You should use plt.plot(pointx, pointy, \'gs\') in your code")

    if code_count == 2:
        print("Code test passed")
        print("Go on to the next step")


def step08(count):
    if count==3:
        print("You scored 3 out of 3. Good job!")

    print("You can go on to the next step")


def step09(code):
    import re
    print(" ")
    if re.search("plt\.plot\(x\,\s*\-x\s*\+\s*3\)", code):
        print("Code test passed")
        print("Go on to the next step")
    elif re.search("plt\.plot\(x\,\s*2\*x\s*\-\s*3\)", code):
        print("Now change the equation and re-run the code.")
    else:
        print("You should use plt.plot(x, -x + 3) in your code.")


# step 10 re-uses step01()


def step11(code):
    import re
    print(" ")
    if re.search("y2\s*\=\s*\-x\s*\-\s*3", code):
        print("Code test passed")
        print("Go on to the next step")
    elif re.search("y2\s*\=\s*x\*\*2\s*\-\s*3", code):
        print("Now change y2 and re-run the code.")
    else:
        print("You should use y2 = -x - 3 in your code.")


def step12(code):
    import re
    print(" ")
    if re.search("linsolve\(\[2\*x\s*\+\s*y\s*\-\s*15\,\s*3\*x\s*\-\s*y\],\s*\(x\,\s*y\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    elif re.search("linsolve\(\[2\*x\s*\+\s*y\s*\-\s*1\,\s*x\s*\-\s*2\*y\s*\+\s*7\]\,\s*\(x\, y\)\)", code):
        print("Now change the equations and re-run the code.")
    else:
        print("You should use linsolve([2*x + y - 15, 3*x - y], (x,y)) in your code.")


# step 13 uses step01()

def step14():
    print(" ")
    print("If you didn't get a syntax error, code test passed")


# steps 15 and 16 re-use step01()


def step17(code):
    import re
    code_count = 0
    first_run = 0

    if re.search("f\(a\,b\)\:", code):
        print("Now change the code and run it again")
        first_run = 1

    if re.search("f\(a\,\s*b\,\s*c\)\:", code):
        code_count = code_count + 1
    elif first_run==1:
        code_count = 0
    else:
        print("You should use f(a,b,c): in your code")

    # plt.plot(x, a*x**2 + b*x + c)
    if re.search("\(x\,\s*a\*x\*\*2\s*\+\s*b\*x\s*\+\s*c\)", code):
        code_count = code_count + 1
    elif first_run==1:
        code_count = 0
    else:
        print("You should use plt.plot(x, a*x**2 + b*x + c) in your code")

    # interactive(f, a=(-9, 9), b=(-9,9), c=(-9,9))
    if re.search("\(f\,\s*a\=\(\-9\,\s*9\)\,\s*b\=\(\-9\,\s*9\)\,\s*c\=\(\-9\,\s*9\)\)", code):
        code_count = code_count + 1
    elif first_run==1:
        code_count = 0
    else:
        print("You should include 'interactive(f, a=(-9, 9), b=(-9,9), c=(-9,9))' in your code")

    if code_count == 3:
        print("Code test passed")
        print("Go on to the next step")

    print(" ")



def step18(code):
    import re
    print(" ")
    code_count = 0
    if re.search("vx\s*\=\s*\-b\/\(2\*a\)", code):
        code_count = code_count + 1
    else:
        print("You should include vx = -b/(2*a)")

    if re.search("vy\s*\=\s*a\*vx\*\*2\s*\+\s*b\*vx\s*\+\s*c", code):
        code_count = code_count + 1
    else:
        print("You should include vy = a*vx**2 + b*vx + c")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step19(code):
    import re
    print(" ")
    # vx = -b/(2*a)
    # vy = a*vx**2 + b*vx + c
    code_count = 0
    if re.search("vx\s*\=\s*\-b\/\(2\*a\)", code):
        code_count = code_count + 1
    else:
        print("You should include vx = -b/(2*a)")

    if re.search("vy\s*\=\s*a\*vx\*\*2\s*\+\s*b\*vx\s*\+\s*c", code):
        code_count = code_count + 1
    else:
        print("You should include vy = a*vx**2 + b*vx + c")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


# step 20 - no test


def step21(code):
    import re
    print(" ")
    code_count = 0
    if re.search("x1\s*\=\s*\(\-b\s*\+\s*math\.sqrt\(b\*\*2\s*\-\s*4\*a\*c\)\)\/\(2\*a\)", code):
        code_count = code_count + 1
    else:
        print("You should include x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)")

    if re.search("x2\s*\=\s*\(\-b\s*\-\s*math\.sqrt\(b\*\*2\s*\-\s*4\*a\*c\)\)\/\(2\*a\)", code):
        code_count = code_count + 1
    else:
        print("You should include x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step22(code):
    import re
    print(" ")
    if re.search("rows\.append\(\[a\,\s*2\*a\]\)", code):
        print("Now change the equation to y = 3x + 2")
    elif re.search("rows\.append\(\[a\,\s*3\*a\+2\]\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include rows.append([a, 3*a+2])")

