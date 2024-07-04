def is_terminal(char):
    return not char.isupper()

def is_non_terminal(char):
    return char.isupper()

def first(rule, prods):
    if len(rule) != 0 and (rule is not None):
        if is_terminal(rule[0]):
            return rule[0]
        elif rule[0] == "#":
            return "#"

    if len(rule) != 0:
        if rule[0] in list(prods.keys()):
            fres = []
            rhs_rules = prods[rule[0]]
            for itr in rhs_rules:
                indivRes = first(itr, prods)
                if type(indivRes) is list:
                    for i in indivRes:
                        fres.append(i)
                else:
                    fres.append(indivRes)

            if "#" not in fres:
                return fres
            else:
                newList = []
                fres.remove("#")
                if len(rule) > 1:
                    ansNew = first(rule[1:], prods)
                    if ansNew != None:
                        if type(ansNew) is list:
                            newList = fres + ansNew
                        else:
                            newList = fres + [ansNew]
                    else:
                        newList = fres
                    return newList
                fres.append("#")
                return fres


def computeAllFirsts(prods):
    first_set={}
    for lhs in list(prods.keys()):
        temp = set()
        for sub in prods.get(lhs):
            res = first(sub, prods)
            if res != None:
                if type(res) is list:
                    for u in res:
                        temp.add(u)
                else:
                    temp.add(res)

        first_set[lhs] = temp

    return first_set
