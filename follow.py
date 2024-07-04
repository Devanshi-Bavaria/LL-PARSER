from first import first

def follow(start_symbol, non_terminal, prods):
    solset = set()
    if non_terminal == start_symbol:
        solset.add('$')
    for curr_non_terminal in prods:
        rhs = prods[curr_non_terminal]
        for subrule in rhs:
            if non_terminal in subrule:
                while non_terminal in subrule:
                    index_nt = subrule.index(non_terminal)
                    subrule = subrule[index_nt + 1:]
                    if len(subrule) != 0:
                        res = first(subrule, prods)
                        if res is None:
                            continue
                        if '#' in res:
                            newList = []
                            res.remove('#')
                            ansNew = follow(start_symbol, curr_non_terminal, prods)
                            if ansNew != None:
                                if type(ansNew) is list:
                                    newList = res + ansNew
                                else:
                                    newList = res + [ansNew]
                            else:
                                newList = res
                            res = newList
                    else:
                        if non_terminal != curr_non_terminal:
                            res = follow(start_symbol, curr_non_terminal, prods)

                    if res is not None:
                        if type(res) is list:
                            for g in res:
                                solset.add(g)
                        else:
                            solset.add(res)
    return list(solset)

def computeAllFollows(start_symbol, prods):
    follow_set = {}
    for non_terminal in prods:
        sol_set = set()
        sol = follow(start_symbol, non_terminal, prods)
        if sol is not None:
            for g in sol:
                sol_set.add(g)
        follow_set[non_terminal] = sol_set

    return follow_set
