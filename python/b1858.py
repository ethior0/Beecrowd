N = int(input());

arr = [int(x) for x in input().split()];
sortedArr = arr.copy();
sortedArr.sort();

print(arr.index(sortedArr[0]) + 1);