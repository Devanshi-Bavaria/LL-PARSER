def removeLeftFactoring(prods):
    new_prods = {}
    for lhs in prods:
        allrhs = prods[lhs]
        temp = dict()
        for subrhs in allrhs:
            if subrhs[0] not in list(temp.keys()):
                temp[subrhs[0]] = [subrhs]
            else:
                temp[subrhs[0]].append(subrhs)
        new_rule = []
        temp_dict = {}
        for term_key in temp:
            allStartingWithTermKey = temp[term_key]
            if len(allStartingWithTermKey) > 1:
                lhs_ = lhs + "'"
                while (lhs_ in prods.keys()) or (lhs_ in temp_dict.keys()):
                    lhs_ += "'"
                new_rule.append([term_key, lhs_])
                ex_rules = []
                for g in temp[term_key]:
                    if(len(g[1:]) == 0):
                        ex_rules.append(['#'])
                    else:
                        ex_rules.append(g[1:])
                temp_dict[lhs_] = ex_rules
            else:
                new_rule.append(allStartingWithTermKey[0])
        new_prods[lhs] = new_rule
        for key in temp_dict:
            new_prods[key] = temp_dict[key]
     
    return new_prods
