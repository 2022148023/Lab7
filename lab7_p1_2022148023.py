with open("input_7_1.txt") as file:
    lines = file.readlines()
    functions = {}
    # iterate over liens
    for line_num in range(len(lines)):
        # look for function definitions
        if "def " in lines[line_num]:
            function_name = lines[line_num].split("(")[0].split(" ")[1]
            functions[function_name] = (line_num + 1, [])
        # look for defined function calls
        else:
            for function in functions.keys():
                if function + "(" in lines[line_num]:
                    functions[function][1].append(line_num + 1)
    for function, lines in functions.items():
        print(f"{function}: def in {lines[0]}, calls in {lines[1]}")
