from operator import indexOf, truediv


def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    elif n==1 or n==2:
        return 1
    memo[n]=fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

def grid(m,n,memo={}):
    key = str(m)+','+ str(n)
    if key in memo:
        return memo[key]
    elif m==0 or n==0:
        return 0
    elif m==1 and n==1:
        return 1
    else:
        memo[key] = grid(m-1,n,memo) + grid(m,n-1,memo)
        return memo[key]

def canSum(target , nums = [], memo = {}):
    if target==0:
        return True
    elif target<0:
        return False
    elif target in memo:
        return memo[target]
    
    for num  in nums:
        remainder = target-num
        memo[remainder] = canSum(remainder, nums,memo)
        if memo[remainder] == True:
            return True
    return False

def howSum(target, nums, memo = {}):
    if target in memo:
        return memo[target]
    elif target == 0:
        return []
    elif target < 0:
        return None
    
    for num in nums:
        remainder = target - num
        remainderResult = howSum(remainder, nums, memo)
        if remainderResult != None:
            memo[target] = remainderResult.append(num)
            return remainderResult
    
    memo[target] = None
    return None

def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n==0 or n==1:
        return 1

    memo[n] = n * factorial(n-1)
    return memo[n]

def bestSum(target, nums, memo = {}):
    if target in memo:
        return memo[target]
    elif target == 0:
        return []
    elif target < 0:
        return None
    
    shortestCombination = None

    for num in nums:
        remainder = target - num
        remainderCombination = bestSum(remainder, nums, memo)
        if remainderCombination != None:
            combination = remainderCombination.copy()
            combination.append(num)
            if shortestCombination == None or len(shortestCombination) > len(combination):
                shortestCombination = combination

    memo[target] = shortestCombination
    return shortestCombination

def canConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    elif target == '':
        return True
    
    for word in wordBank:
        if word in target:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if canConstruct(suffix, wordBank, memo) == True:
                    memo[target] = True
                    return True
    memo[target]=False
    return False

def countConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    elif target == '':
        return 1

    totalCount = 0
    
    for word in wordBank:
        if word in target:
            if target.index(word) == 0:
                suffix = target[len(word):]
                numWays = countConstruct(suffix, wordBank, memo)
                totalCount += numWays
    memo[target]=totalCount
    return totalCount

def allConstruct(target, wordBank, memo={}):
    if target == '':
        return [[]]
    elif target in memo:
        return memo[target]
    
    result = []

    for word in wordBank:
        if word in target:
            if target.index(word)==0:
                suffix = target[len(word):]
                suffixWays = allConstruct(suffix, wordBank, memo)
                targetWays = list(word) + suffixWays
                result.append(targetWays)
    return result

def fibo(n):
    tab = [0]*(n+2)
    tab[1] = 1
    for i in range(n):
        tab[i+1] += tab[i]
        tab[i+2] += tab[i]
    return tab[n]

def grido(m, n):
    tab = [[0]*(n+2) for row in range(m+2)]
    tab[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            tab[i+1][j] += tab[i][j]
            tab[i][j+1] += tab[i][j]
    return tab[m][n]

def canSumo(target, numbers):
    tab = [False]*(target+1)
    tab[0] = True
    for i in range(target):
        if tab[i] == True:
            for num in numbers:
                if (i+num) <= target:
                    tab[i+num]=True
    return tab[target]

def howSumo(target, numbers):
    tab = [None]*(target+1)
    tab[0] = []
    for i in range(target):
        if tab[i] != None:
            for num in numbers:
                if (i+num) <= target:
                    tab[i+num] = tab[i].copy()
                    tab[i+num].append(num)
    return(tab[target])
    
def bestSumo(target, numbers):
    tab = [None]*(target+1)
    tab[0] = []
    for i in range(target):
        if tab[i] != None:
            for num in numbers:
                if (i+num) <= target and tab[i+num]==None:
                    tab[i+num] = tab[i].copy()
                    tab[i+num].append(num)
    return(tab[target])

def canConstructo(string, wordBank):
    tab = [False]*(len(string)+1)
    tab[0] = True
    for i in range(len(string)+1):
        if tab[i] == True:
            for word in wordBank:
                if word in string and string.index(word)==i:
                    tab[i+len(word)]=True
    return tab[len(string)]

def countConstructo(string, wordBank):
    tab = [0]*(len(string)+1)
    tab[0] = 1
    for i in range(len(string)+1):
        if tab[i] > 0:
            for word in wordBank:
                if word in string and string.index(word)==i:
                    tab[i+len(word)]+=1
    return tab[len(string)]

def howConstructo(string,wordBank):
    tab = [None]*(len(string)+1)
    tab[0] = []
    for i in range(len(string)+1):
        if tab[i] != None:
            for word in wordBank:
                if word in string and string.index(word)==i:
                    if tab[i+len(word)]!= None:
                        tab[i+len(word)].append(tab[i].copy())
                    else:
                        tab[i+len(word)] = tab[i].copy()
                        tab[i+len(word)].append(word)
    return tab[len(string)]

def areAnagrams(string1, string2):
    map1 = {}
    map2 = {}
    if len(string1) != len(string2): return False
    for ch in string1:
        if ch in map1:
            map1[ch]+=1
        else:
            map1[ch]=1
    for ch in string2:
        if ch in map2:
            map2[ch]+=1
        else:
            map2[ch]=1
    for ch in map1:
        if map1[ch] != map2[ch]: return False
    return True

def firstAndLast(arr, target):
    if len(arr)==0 or arr[0] > target or arr[-1]<target:
        return [-1,-1]
    left,right = 0, len(arr)-1
    mid = (left+right)/2
    
    

def gridChallenge(grid):
    # Write your code here
    for row in grid:
        l = list(row)
        l.sort()
        row = ''.join(l)
    for i in range(len(grid[0])):
        for j in range(len(grid)-1):
            if ord(grid[j][i]) > ord(grid[j+1][i]):
                return "NO"
    return "YES"

def flippingMatrix(matrix):
    # Write your code here
    n=len(matrix)//2
    for row in matrix:
        if sum(row[0:n]) < sum(row[n:(2*n)]):
            row = row[::-1]
            print(row)


def superDigit(n, k):
    # Write your code here
    digit = n*k
    digit = list(digit)
    while sum(digit) > 9:
        digit = list(str(sum(digit)))
    return sum(digit)