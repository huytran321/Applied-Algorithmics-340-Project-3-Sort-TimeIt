# Made by Huy Tran
# Bigo module with the four find functions

def find1(list, val):
    for i in range(len(list)):
        if list[i] == val:
            return True
    return False

def find2(list, val):
    tempList = []
    tempList[:] = list[:]
    tempList.sort()
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if tempList[mid] == val:
            return True
        elif tempList[mid] < val:
            low = mid + 1
        elif tempList[mid] > val:
            high = mid - 1
    return False
            
def find3(list, val):
    if val in list:
        return True
    else:
        return False

def find4(list, val):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == val:
            return True
        elif list[mid] < val:
            low = mid + 1
        elif list[mid] > val:
            high = mid - 1
    return False
