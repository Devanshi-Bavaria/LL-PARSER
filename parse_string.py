from parse_table import return_terminals
import pandas as pd


def custom_reverse(string):
    print("string: ", string)

    rev_string = string[::-1]
    rev_list = list(rev_string)
    i = 0

    while i < (len(rev_list)):
        print(i, rev_list)
        if rev_list[i] == "'":
            print(i, rev_list[i])
            if i + 1 >= len(rev_list):
                print("Outside range: ", i)
                continue
            rev_list[i], rev_list[i + 1] = rev_list[i + 1], rev_list[i]
            i += 1
        print(rev_list)
        i += 1
        # print(i)
    return "".join(rev_list)


def parsingUsingStack(prods, parse_table, ll_grammar, input_string, start_symbol):
    return_string = ""

    if ll_grammar == False:
        return_string = "Grammar is not LL(1)"
        return return_string, None

    non_terminals = list(prods.keys())

    terminals = list(return_terminals(prods))
    terminals.sort()
    terminals.append("$")

    stack = []
    input = []
    action = []

    # initial
    stack.append("$" + start_symbol)
    input.append(input_string + "$")
    action.append(" ")

    input_string += "$"
    stack_string = "$" + start_symbol
    i = 0
    n = len(input_string)

    while True and i != n:
        curr_string = input_string[0]
        curr_top = stack_string[-1]
        stack_string = stack_string[:-1]
        if curr_top == "'":
            curr_top = stack_string[-1] + curr_top
            stack_string = stack_string[:-1]
        # print("Debug: ", curr_top, curr_string)

        if curr_top == "#":
            continue

        if curr_string not in terminals:
            return_string = "Wrong Input Character " + str(curr_string)
            df = pd.DataFrame({"Stack": stack, "Input": input, "Action": action})
            return return_string, df

        if curr_top == "$" and curr_string == "$":
            stack.append(curr_top)
            input.append(curr_string)
            action.append("Accepted")
            return_string = "String accepted"
            df = pd.DataFrame({"Stack": stack, "Input": input, "Action": action})
            return return_string, df

        if curr_string != "$" and curr_top == "$":
            return_string = "Invalid input string"
            df = pd.DataFrame({"Stack": stack, "Input": input, "Action": action})
            return return_string, df

        if curr_top in non_terminals:
            non_terminal_index = non_terminals.index(curr_top)

            if parse_table[curr_string][non_terminal_index] == "":
                return_string = "Invalid input string"
                df = pd.DataFrame({"Stack": stack, "Input": input, "Action": action})
                return return_string, df
            else:
                production = parse_table[curr_string][non_terminal_index]
                rhs = production.split(" -> ")[1]
                rhs = custom_reverse(rhs)
                stack_string += rhs

            stack.append(stack_string)
            input.append(input_string)
            action.append(production)

        else:
            if curr_top == curr_string:
                input_string = input_string[1:]
                stack.append(stack_string)
                input.append(input_string)
                action.append("Pop " + curr_string)
                i += 1
                continue
            else:
                return_string = "Invalid input string"
                df = pd.DataFrame({"Stack": stack, "Input": input, "Action": action})
                return return_string, df

    print("String parsed")
    print(stack, input, action)

    return_string = "String accepted"
    df = pd.DataFrame({"Stack": stack, "Input": input, "Action": action})

    return return_string, df
