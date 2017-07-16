import itertools as it

max_card = 13
cards = [x+1 for x in list(range(max_card))]
allcombos = list(it.product(cards,repeat=4))
allhands = list(set([tuple(sorted(list(x))) for x in allcombos]))

def f1(x,y): return x + y
def f2(x,y): return x * y
def f3(x,y): return x - y
def f4(x,y): return y - x
def f5(x,y):
    if y == 0: return 0
    else: return x / y
def f6(x,y):
    if x == 0: return 0
    else: return y / x
    
funlist = [f1,f2,f3,f4,f5,f6]
symlist = [["+",-1],["*",-1],["-",0],["-",1],["/",0],["/",1]]

funcombos = []
for i in funlist:
    for j in funlist:
        for k in funlist:
            funcombos += [[i,j,k]]

def printsol(a,b,func):
    if symlist[funlist.index(func)][1] == 1:
        arg = b+symlist[funlist.index(func)][0]+a
    elif symlist[funlist.index(func)][1] == 0:
        arg = a+symlist[funlist.index(func)][0]+b
    else :
        arg = min(a,b)+symlist[funlist.index(func)][0]+max(a,b)
    return "("+arg+")"

def convert(solution):
    num = [str(x) for x in solution[0]]
    func = solution[1]
    type = solution[2]
    if type == 1:
        return printsol(printsol(printsol(num[0],num[1],func[0]),num[2],func[1]),num[3],func[2])
    else:
        return printsol(printsol(num[0],num[1],func[0]),printsol(num[2],num[3],func[1]),func[2])

def get_solutions(hand):
    combos = list(set(list(it.permutations(hand))))

    solutions = []
    output = []

    for i in combos:
        for j in funcombos:
            if j[2](j[1](j[0](i[0],i[1]),i[2]),i[3]) == 24:
                solutions += [[i,j,1]]
            if j[2](j[0](i[0], i[1]), j[1](i[2], i[3])) == 24:
                solutions += [[i,j,2]]

    for i in solutions:
        output += [convert(i)[1:-1]]

    return list(set(output))

def all_solutions():
    solutions = []
    for i in allhands:
        solutions += [[i,get_solutions(i)]]
    return solutions

