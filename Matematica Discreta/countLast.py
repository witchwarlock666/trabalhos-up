arr = [1]
newArr = []
i = 0
j = 0

def nextValue(k, val, count):
    try:
        nextVal = arr[k+1]
    except:
        return count
    if (nextVal == val):
        count += 1
        count = nextValue(k+1,val, count)
    return count

while (i < 10):
    print(arr)
    j = 0

    while (j < len(arr)):
        count = 1
        val = arr[j]
        count = nextValue(j, val, count)
        newArr.append(count)
        newArr.append(val)
        j += count
    arr = newArr
    newArr = []
    i += 1
