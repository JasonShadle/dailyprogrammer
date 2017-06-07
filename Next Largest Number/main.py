import itertools
initNum = input('Enter the number:')

nums = list(int(x) for x in str(initNum))

permutation = list(itertools.permutations(nums))

permutation.sort()

ind = permutation.index(tuple(nums))
ind += 1
#print((int(permutation[ind][0])))
for x in range(0, len(permutation[ind])):
    print(permutation[ind][x], end='')
