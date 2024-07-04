def process_user_input(prods):
    processed_input = {}

    for prod in prods.split("\n"):
        temp = prod.split("->")
        # print(temp)
        
        if len(temp) > 1:
            lhs = temp[0].strip()
            rhs = temp[1]

            rhs_prods = rhs.split("|")
            rhs_prods_temp = [list(x.strip()) for x in rhs_prods]
            processed_input[lhs] = rhs_prods_temp
            # print("------------------------------")
        
    # print(processed_input)
    return processed_input

def print_dictionary(dict):
    final_str = []
    for lhs in dict:
        full_rhs = dict[lhs]
        temp_list = []
        for rhs in full_rhs:
            str = "".join(rhs)
            temp_list.append(str)
        new_rhs = " | ".join(temp_list)
        final_str.append(lhs + " -> " + new_rhs)
    return final_str