# Removes leading and trailing dots and collapsed consecutive dots
def preprocessInputString(inputString: str) -> str:
    ret = ""
    curIdx = 0
    
    # move to first "?"" or "#""
    while curIdx < len(inputString) and inputString[curIdx] == '.':
        curIdx += 1

    # copy content over, collapse consecutive dots in the process
    prev = None
    while curIdx < len(inputString):
        cur = inputString[curIdx]

        if cur == '.' and prev == '.':
            curIdx += 1
            continue
        
        ret += cur
        prev = cur
        curIdx += 1

    # remove trailing dots
    numTrailing = 0
    while ret[-numTrailing - 1] == '.':
        curIdx -= 1
        numTrailing += 1

    if numTrailing != 0:
        ret = ret[0:-numTrailing]

    return ret

def buildStringFromGuess(stringLength: int, numbers: list, guess: list) -> str:
    ret = ""
    for i in range(len(guess)):
        ret += "." * guess[i]
        ret += "#" * numbers[i]

    fillChar = '.' if len(numbers) == len(guess) else '?'
    ret += fillChar * (stringLength - len(ret))
    return ret

def doStringsMatch(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        c1: chr = str1[i]
        c2: chr = str2[i]

        if (c1 == '.' and c2 == '#') or (c1 == '#' and c2 == '.'):
            return False
        
    return True


def solveRecursivelyByExtendingGuesses(currentGuesses: list, compStr: str, numbers: list) -> int:
    # This has to be valid, otherwise this recursion wouldn't have been taken
    if len(currentGuesses) == len(numbers):
        # print(
        #     f"found match with guesses {currentGuesses}" +
        #     f"(string is {buildStringFromGuess(len(compStr), numbers, currentGuesses)}, " +
        #     f"comp is {compStr})"
        # )
        return 1
    
    numRemainingGuesses: int = len(numbers) - len(currentGuesses)
    minGuess = 0 if len(currentGuesses) == 0 else 1
    maxGuess: int = len(compStr) - sum(numbers) - sum(currentGuesses) - (numRemainingGuesses - 1)

    total = 0
    newGuesses = list(currentGuesses)
    newGuesses.append(0)
    for i in range(minGuess, maxGuess + 1):
        # print((" " * len(currentGuesses)) + f"doing guess {i}")
        newGuesses[-1] = i
        guessStr: str = buildStringFromGuess(len(compStr), numbers, newGuesses)

        if not doStringsMatch(guessStr, compStr):
            continue

        total += solveRecursivelyByExtendingGuesses(newGuesses, compStr, numbers)

    return total