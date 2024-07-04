from first import first


def return_terminals(prods):
    terminals = []
    for prod in prods:
        for rhs in prods.get(prod):
            for rhs_item in rhs:
                if not rhs_item.isupper():
                    terminals.append(rhs_item)
    return set(terminals)


def createParseTable(prods, first_set, follow_set):
    import copy

    non_terminals = list(prods.keys())
    terminals = list(return_terminals(prods))
    terminals.sort()
    terminals.append("$")

    parse_table = {}
    for terminal in terminals:
        if terminal == "#":
            continue
        temp_list = ["" for i in range(len(non_terminals))]
        parse_table[terminal] = temp_list

    print(parse_table)
    grammar_is_LL = True

    for lhs in prods:
        rhs = prods[lhs]
        for y in rhs:
            res = first(y, prods)
            # print("Rhs: ", y)
            if res is None:
                # print("None")
                continue
            if "#" in res:
                if type(res) == str:
                    firstFollow = []
                    fol_op = follow_set[lhs]
                    if fol_op is str:
                        firstFollow.append(fol_op)
                    else:
                        for u in fol_op:
                            firstFollow.append(u)
                    res = firstFollow
                else:
                    res.remove("#")
                    res = list(res) + list(follow_set[lhs])

            # Add rules to table
            ttemp = []
            if type(res) is str:
                ttemp.append(res)
                res = copy.deepcopy(ttemp)
            for terminal in res:
                lhs_index = non_terminals.index(lhs)
                if parse_table[terminal][lhs_index] == "":
                    parse_table[terminal][lhs_index] = (
                        parse_table[terminal][lhs_index] + f"{lhs} -> {''.join(y)}"
                    )
                else:
                    # if rule already present
                    if f"{lhs}->{y}" in parse_table[terminal][lhs_index]:
                        continue
                    else:
                        grammar_is_LL = False
                        parse_table[terminal][lhs_index] = (
                            parse_table[terminal][lhs_index] + f",{lhs} -> {''.join(y)}"
                        )

    print(parse_table)
    return (parse_table, grammar_is_LL, non_terminals)
