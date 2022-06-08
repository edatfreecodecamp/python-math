# Tests for Foundational Math Cert 4

def step00():
    print("Code test passed")
    print("Go on to the next step")


def step01(code):
    import re
    print(" ")
    # verts = [(0., 0.), (0., 2.), (2., 2.), (2., 0.), (0., 0.),]
    # verts = [(0., 0.), (-1., 1.), (0., 2.), (2., 2.), (3., 1.), (2., 0.), (0., 0.),]
    if re.search("verts\s*\=\s*\[\(0\.\,\s*0\.\)\,\s*\(0\.\,\s*2\.\)\,\s*\(2\.\,\s*2\.\)\,\s*\(2\.\,\s*0\.\)\,\s*\(0\.\,\s*0\.\)\,\s*\]", code):
        print("Now change the code and run it again.")
    elif re.search("verts\s*\=\s*\[\(0\.\,\s*0\.\)\,\s*\(\-1\.\,\s*1\.\)\,\s*\(0\.\,\s*2\.\)\,\s*\(2\.\,\s*2\.\)\,\s*\(3\.\,\s*1\.\)\,\s*\(2\.\,\s*0\.\)\,\s*\(0\.\,\s*0\.\)\,\s*\]", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use verts = [(0., 0.), (-1., 1.), (0., 2.), (2., 2.), (3., 1.), (2., 0.), (0., 0.),] in your code")


def step02(code):
    import re
    print(" ")
    code_count = 0
    # input
    if re.search("c\_string\s*=\s*input\(\"Side\s*c\s*=\s*\"\)", code):
        code_count = code_count + 1
    else:
        print("You should use c_string = input(\"Side c = \") in your code")

    # if
    if re.search("if\s*\(c\_string\s*\=\=\s*\"c\"\)\:", code):
        code_count = code_count + 1
    else:
        print("You should use if (c_string==\"c\"): in your code")

    # formula
    if re.search("c\s*=\s*math\.sqrt\(a\*\*2\s*\+\s*b\*\*2\)", code):
        code_count = code_count + 1
    else:
        print("You should use c = math.sqrt(a**2 + b**2) in your code")

    # print
    if re.search("print\(\"c\s*=\s*\"\,\s*c\)", code):
        code_count = code_count + 1
    else:
        print("You should use print(\"c = \", c) in your code")

    # code count
    if code_count==4:
        print("Code test passed")
        print("Go on to the next step")


def step03():
    print("Notice how the distance is the hypotenuse")
    print("Go on to the next step")


def step04(code):
    import re
    print(" ")
    code_count = 0

    # x2 = float(second[0])
    if re.search("x2\s*\=\s*float\(second\[0\]\)", code):
        code_count = code_count + 1
    else:
        print("You should use x2 = float(second[0]) in your code")

    # y2 = float(second[1])
    if re.search("y2\s*\=\s*float\(second\[1\]\)", code):
        code_count = code_count + 1
    else:
        print("You should use y2 = float(second[1]) in your code")

    # distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if re.search("distance\s*\=\s*math\.sqrt\(\(x2\-x1\)\*\*2\s*\+\s*\(y2\-y1\)\*\*2\)", code):
        code_count = code_count + 1
    else:
        print("You should use distance = math.sqrt((x2-x1)**2 + (y2-y1)**2) in your code")

    # code count
    if code_count==3:
        print("Code test passed")
        print("Go on to the next step")


def step05(code):
    import re
    print(" ")
    code_count = 0
    # x = (x1+x2)/2
    if re.search("x\s*\=\s*\(x1\s*\+\s*x2\)\/2", code):
        code_count = code_count + 1
    else:
        print("You should use x = (x1+x2)/2 in your code")

    # y = (y1+y2)/2
    if re.search("y\s*\=\s*\(y1\s*\+\s*y2\)\/2", code):
        code_count = code_count + 1
    else:
        print("You should use y = (y1+y2)/2 in your code")

    # code count
    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step06():
    print("Notice the description of each side")
    print("Go on to the next step")


def step07():
    print("Notice how the description of each side changed")
    print("Go on to the next step")


def step08():
    print("Notice the different ratios for A and B")
    print("Go on to the next step")


def step09(code):
    import re
    print(" ")
    code_count = 0
    if re.search("sinA\s*\=\s*opp\/hyp", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use sinA = opp/hyp in your code")


def step10():
    print(" ")
    print("Notice the different ratios for A and B")
    print("Go on to the next step")


def step11(code):
    import re
    print(" ")
    code_count = 0
    if re.search("cosA\s*\=\s*adj\/hyp", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use cosA = adj/hyp in your code")


def step12():
    print(" ")
    print("Notice the different ratios for A and B")
    print("Go on to the next step")


def step13(code):
    import re
    print(" ")
    if re.search("tanA\s*\=\s*opp\/adj", code):
        print("Code test passed")
        print("Go to the next step")
    else:
        print("You should use tanA = opp/adj in your code")


def step14(code):
    import re
    print(" ")
    code_count = 0
    # cosA_actual = round(b/c,4)
    if re.search("cosA\_actual\s*\=\s*round\(b\/c\,4\)", code):
        code_count = code_count + 1
    else:
        print("You should use cosA_actual = round(b/c,4) in your code")

    # tanA_actual = round(a/b,4)
    if re.search("tanA\_actual\s*\=\s*round\(a\/b\,4\)", code):
        code_count = code_count + 1
    else:
        print("You should use tanA_actual = round(a/b,4) in your code")

    # sinB_actual = round(b/c,4)
    if re.search("sinB\_actual\s*\=\s*round\(b\/c\,4\)", code):
        code_count = code_count + 1
    else:
        print("You should use sinB_actual = round(b/c,4) in your code")

    # cosB_actual = round(a/c,4)
    if re.search("cosB\_actual\s*\=\s*round\(a\/c\,4\)", code):
        code_count = code_count + 1
    else:
        print("You should use cosB_actual = round(a/c,4) in your code")

    # tanB_actual = round(b/a,4)
    if re.search("tanB\_actual\s*\=\s*round\(b\/a\,4\)", code):
        code_count = code_count + 1
    else:
        print("You should use tanB_actual = round(b/a,4) in your code")

    if code_count==5:
        print("Code test passed")
        print("Go to the next step")


def step15(code):
    import re
    print(" ")
    code_count = 0
    if re.search("round\(math\.cos\(math\.radians\(angle\)", code):
        print("Code test passed")
        print("Go to the next step")
    else:
        print("Your code should include ratio_c = round(math.cos(math.radians(angle)),4)")


# step 16  re-uses step 00


def step17():
    print(" ")
    print("Look at the triangle and notice the pattern")
    print("Go to the next step")
    print(" ")


def step18():
    print("See how the sin() and cos() relate to points on the circle")
    print("Go on to the next step")


def step19(code):
    import re
    print(" ")
    code_count = 0
    # = round(math.cos(math.radians(rangle)), 4)
    if side_b==0:
        print("Scroll up to see the example, then write the code to solve for b")
    elif re.search("\=\s*round\(math\.cos\(math\.radians\(rangle\)\)\,\s*4\)", code):
        code_count = code_count + 1
    else:
        print("Your code should include cos_value = round(math.cos(math.radians(rangle)), 4)")

    # side_b = round(sideC*cos_value,2)
    if side_b==0:
        print(" ")
    elif re.search("side\_b\s*\=\s*round\(sideC\*cos\_value\,2\)", code):
        code_count = code_count + 1
    else:
        print("Your code should include side_b = round(sideC*cos_value,2)")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step20(code):
    import re
    print(" ")
    code_count = 0
    # sideA/math.sin(radian_angle)
    if sideC==0:
        print("Now write the code to solve for sideC")
    elif re.search("sideA\/math\.sin\(radian\_angle\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include sideC = sideA/math.sin(radian_angle)")


def step21(code):
    import re
    print(" ")
    code_count = 0
    # sideA/math.cos(radian_angle)
    if sideC==0:
        print("Now write the code to solve for the diagonal force")
    elif re.search("sideA\/math\.cos\(radian\_angle\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include sideC = sideA/math.cos(radian_angle)")


def step22(code):
    import re
    print(" ")
    code_count = 0
    # sideA/math.tan(radian_angle)
    if sideB==0:
        print("Now write the code to solve for the distance")
        print(" ")
    elif re.search("sideA\/math\.tan\(radian\_angle\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include sideC = sideA/math.cos(radian_angle)")


def step23(code):
    import re
    print(" ")
    code_count = 0
    # side_B = math.sin(math.radians(angle_B))*sideA/math.sin(math.radians(angleA))
    if sideB==0:
        print("Now write the code to solve for side b")
        print(" ")
    elif re.search("side\_B\s*\=\s*math\.sin\(math\.radians\(angle\_B\)\)\*sideA\/math\.sin\(math\.radians\(angleA\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include side_B = math.sin(math.radians(angle_B))*sideA/math.sin(math.radians(angleA))")


def step24(code):
    import re
    print(" ")
    code_count = 0
    # almost = sideA**2 + sideB**2 - 2*sideA*sideB*math.cos(math.radians(angle_C))
    # side_C = math.sqrt(almost)
    if side_C==0:
        print("Now write the code to solve for side c")
        print(" ")
    elif re.search("sideA\*\*2\s*\+\s*sideB\*\*2\s*\-\s*2\*sideA\*sideB\*math\.cos\(math\.radians\(angle\_C\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include side_C = math.sqrt(sideA**2 + sideB**2 - 2*sideA*sideB*math.cos(math.radians(angle_C)))")


def step25(code):
    import re
    print(" ")
    code_count = 0
    # area = 0.5*sideA*sideB*math.sin(math.radians(angleC))
    if area==0:
        print("Now write the code to find the area")
        print(" ")
    elif re.search("area\s*\=\s*0\.5\*sideA\*sideB\*math\.sin\(math\.radians\(angleC\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include area = 0.5*sideA*sideB*math.sin(math.radians(angleC))")


# no test for step 26


def step27():
    print("Notice the pattern, then go on to the next step")
    print(" ")


# no test for step 28


def step29():
    print("Notice which frequency combinations produce more regular patterns \n")


