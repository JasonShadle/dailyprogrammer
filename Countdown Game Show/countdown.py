# I went for the fastest answer, did not go for efficiency
import itertools
count = 0
numbers = input('Enter the numbers:')
op = {0:'+',1:'-',2:'*',3:'/'}
# set is a non-repeatable array. ex: if it is (1,2,3) and I add 2, it is still (1,2,3)
ans = set()

numbersArr = numbers.split(' ')
answer = numbersArr[6]

# grabs all permutations
perms = itertools.permutations(numbersArr[:-1])

for perm in perms:
    # loops through all permutations
    for a in range(0,4):
        for b in range(0,4):
            for c in range(0,4):
                for d in range(0,4):
                    for e in range(0,4):
                        # makes a string to evaluate left to right and avoid PEMDAS
                        numStr = '(((((' + str(perm[0]) + op[a] + str(perm[1]) + ')' + op[b] + str(perm[2]) + ')'+\
                              op[c] + str(perm[3]) + ')' + op[d] + str(perm[4]) + ')' + op[e] + str(perm[5])+ ')'
                        num = eval(numStr)
                        if int(num) == int(answer):
                            # adds to list
                            ans.add(numStr)

# prints the set
for z in ans:
    print(z)