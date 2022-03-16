# Tests for Foundational Math Cert 1

def step01(code):
    import re
    print(" ")
    if re.search("print\s*\(\s*a\s*\+\s*b\s*\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use print(a + b) in your code")


def step02(code):
    import re
    print(" ")
    if re.search("print\s*\(\s*c\s*\-\s*d\s*\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use print(c - d) in your code")


def step03(code):
    import re
    print(" ")
    if re.search("print\s*\(\s*[e]\s*\*\s*[f]\s*\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use print(e * f) in your code")


def step04(code):
    import re
    print(" ")
    if re.search("print\s*\(\s*[g]\s*\/\s*[h]\s*\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use print(g/h) in your code")


def step05(code):
    import re
    print(" ")
    if re.search("intB\s*\=\s*int\(strB\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use intB = int(strB) in your code")


def step06(code):
    import re
    print(" ")
    #intA = int(input('Enter an integer: '))
    if re.search("intB\s*\=\s*int\(input\(\'Enter an integer\:\s*\'\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use intB = int(input('Enter an integer: ')) in your code")


def step07(code):
    import re
    print(" ")
    #b = float(input('Enter a number: '))
    if re.search("b\s*\=\s*float\(input\(\'Enter a number\:\s*\'\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use b = float(input('Enter a number: ')) in your code")


def step08(answer):
    print(" ")
    if answer==8:
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You can try again if you like")


def step09(code):
    import re
    print(" ")
    # print(a%b)
    if re.search("print\(a\s*\%\s*b\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use print(a % b) in your code")


def step10(code):
    import re
    print(" ")
    if re.search("if number\s*\%\s*test\_factor\s*\=\=\s*0\:", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("You should use if number % test_factor == 0: in your code")


def step11(code):
    import re
    print(" ")
    if re.search("if number\s*\%\s*test\_factor\s*\=\=\s*0:", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include if number % test_factor == 0:")


def step12(code):
    import re
    print(" ")
    if re.search("if test\_number\:", code):
        print("Now change the if statement")
    elif re.search("if number\s*\%\s*test\_number\=\=0\:", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include if number % test_number == 0:")


def step13(code):
    import re
    print(" ")
    if re.search("print\(1\/n\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include print(1/n)")


def step14(code):
    import re
    print(" ")
    if re.search("b\s*=\s*float\(sp\[1\]\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include b = float(sp[1])")


def step15(code):
    import re
    print(" ")
    if re.search("print\(n\*\*2\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include print(n**2)")


def step16(code):
    import re
    print(" ")
    if re.search("print\(math\.sqrt\(n\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include print(math.sqrt(n))")


def step17(code):
    import re
    print(" ")
    if re.search("print\(math\.floor\(n\)\)", code):
        print("Code test passed")
        print("Go on to the next step")
    else:
        print("Your code should include print(math.floor(n))")


def step18(code):
    import re
    print(" ")
    code_count=0
    code = In[-1].split('# Only change code above this line')[0];

    # if n % (maybe_factor**2) == 0:
    if re.search("if n\s*\%\s*\(maybe\_factor\*\*2\)\s*\=\=\s*0\:", code):
        code_count = code_count + 1
    else:
        print("Your code should include if n % (maybe_factor**2) == 0:")

    # max_factor = maybe_factor
    if re.search("max\_factor\s*\=\s*maybe\_factor", code):
        code_count = code_count + 1
    else:
        print("Your code should include max_factor = maybe_factor")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step19():
    print("\n Test passed. You can go on to the next step.")


def step20():
    print("\n Test passed. This is this your factored square root:\n")


def step21(code):
    import re
    print(" ")
    code_count = 0
    code = In[-1].split('# Only change code above this line')[0];
    if re.search("print\(round\(a\,\s*\-6\)", code):
        code_count = code_count + 1
    else:
        print("Your code should inlcude 'print(round(a,-6)'")
     
    if re.search("print\(round\(b\,\s*3\)", code):
        code_count = code_count + 1
    else:
        print("Your code should inlcude 'print(round(b,3)'")

    if code_count == 2:
        print("Code test passed")
        print("Go on to the next step")


def step22():
    print(" ")
    # one solution
    numerator2 = int(n*10**exponent)
    denominator2 = 10**exponent
    percent2 = n*100
    code_count = 0
    if numerator2==numerator:
        code_count = code_count + 1
    else:
        print("You should use numerator = int(n*10**exponent) in your code")

    if denominator2==denominator:
        code_count = code_count + 1
    else:
        print("You should use denominator = 10**exponent in your code")

    if percent2==percent:
        code_count = code_count + 1
    else:
        print("You should use percent = n*100 in your code")

    if code_count==3:
        print("Code test passed")
        print("Go on to the next step")


def step23(code):
    import re
    print(" ")
    code_count = 0
    if re.search("def say\_something\(\)\:", code):
        print("Now change the name of the function")
    elif re.search("def fun\(\)\:", code):
        code_count = code_count+1
    else:
        print("You should include def fun(): in your code")

    if re.search("\nsay\_something\(\)", code):
        print("Also remember to call the function")
    elif re.search("\nfun\(\)\s*", code):
        code_count = code_count+1
    else:
        print("Remember to call the function fun() in your code")

    if code_count==2:
        print("Code test passed")
        print("Go on to the next step")


def step24(code):
    import re
    print(" ")
    code_count = 0
    if re.search("nom\s*\=\s*input", code):
        print("Now change the variable name from 'nom' to 'nombre'")
    elif re.search("nombre\s*\=\s*input", code):
        code_count = code_count + 1
    else:
        print("Your code should include nombre = input(...")

    if re.search("greeting\(nom\)", code):
        print("Now change the argument when you call the function")
    elif re.search("greeting\(nombre\)", code):
        code_count = code_count + 1
    else:
        print("Your code should include greeting(nombre)")

    if code_count==2:
        print("Code test passed")
        print("You can go on to the next step")


def step25(code):
    import re
    print(" ")
    code_count = 0
    if re.search("add\(first\,\s*second\)", code):
        print("Now include the third variable when you call the function")
    elif re.search("add\(first\,\s*second\,\s*third\)", code):
        code_count = code_count + 1
    else:
        print("Your code should include add(first,second,third)")

    if re.search("def add\(a\,\s*b\)\:", code):
        print("Now change the argument when you define the function")
    elif re.search("def add\(a\,\s*b\,\s*c\)\:", code):
        code_count = code_count + 1
    else:
        print("Your code should include def add(a,b,c):")

    if re.search("sum\s*\=\s*a\s*\+\s*b\s*\+\s*c", code):
        code_count = code_count + 1
    elif re.search("sum\s*\=\s*a\s*\+\s*b", code):
        print("Now change the sum line in the function")
    else:
        print("Your code should include sum = a + b + c")

    if code_count==3:
        print("Code test passed")
        print("You can go on to the next step")


def step26(code):
    import re
    print(" ")
    code_count = 0
    if re.search("return number\*2", code):
        print("Now change the return statement in the function")
    elif re.search("return number\*3", code):
        print("Code test passed")
        print("You can go on to the next step")
    else:
        print("Your code should include return number*3")


def step27(code):
    print("If you didn't get a syntax error, you are ready for the project")

# probably add 3 more steps
