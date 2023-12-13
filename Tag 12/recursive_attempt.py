import copy
from datastructures import *

# Returns number of successful attempts
def attemptRecursively(attempt: RowAttempt, curSpringIdx: int, curNumberIdx: int) -> int:
    lastChainSet: bool = curNumberIdx == len(attempt.row.springNumbers)

    # Move to first gear that is not operational
    while curSpringIdx < attempt.row.getLength() and attempt.getStateAtIdx(curSpringIdx) == DescriptorRow.STATE_OPERATIONAL:
        curSpringIdx += 1

    # If we hit end, we better be finished
    if curSpringIdx >= attempt.row.getLength():
        return 1 if lastChainSet else 0

    # If we hit a broken gear, it needs to be the next consecutive chain of broken gears
    if attempt.getStateAtIdx(curSpringIdx) == DescriptorRow.STATE_BROKEN:
        if lastChainSet:
            return 0

        curNumber = attempt.row.springNumbers[curNumberIdx]
        putChainSuccess = _putBrokenChain(attempt, curSpringIdx, curNumber)
        if putChainSuccess:
            return attemptRecursively(attempt, curSpringIdx + curNumber + 1, curNumberIdx + 1)
        else:
            return 0
        
    # If we hit an unknown gear, we can either make it broken or operational
    newAttempt1: RowAttempt = copy.deepcopy(attempt)
    newAttempt2: RowAttempt = copy.deepcopy(attempt)
    newAttempt1.putAttempt(curSpringIdx, DescriptorRow.STATE_OPERATIONAL)
    newAttempt2.putAttempt(curSpringIdx, DescriptorRow.STATE_BROKEN)

    return attemptRecursively(newAttempt1, curSpringIdx, curNumberIdx) + attemptRecursively(newAttempt2, curSpringIdx, curNumberIdx)



# returns True if chain was successfully put
def _putBrokenChain(attempt: RowAttempt, curSpringIdx: int, number: int) -> bool:
    for i in range(curSpringIdx, curSpringIdx + number):
        if i >= attempt.row.getLength():
            return False

        state = attempt.getStateAtIdx(i)

        if state == DescriptorRow.STATE_OPERATIONAL:
            return False
        
        if state == DescriptorRow.STATE_UNKNOWN:
            attempt.putAttempt(i, DescriptorRow.STATE_BROKEN)

    idxAfterChain = curSpringIdx + number
    if idxAfterChain == attempt.row.getLength():
        return True
    
    stateAfterChain = attempt.getStateAtIdx(idxAfterChain)
    if stateAfterChain == DescriptorRow.STATE_BROKEN:
        return False
    elif stateAfterChain == DescriptorRow.STATE_UNKNOWN:
        attempt.putAttempt(idxAfterChain, DescriptorRow.STATE_OPERATIONAL)

    return True
