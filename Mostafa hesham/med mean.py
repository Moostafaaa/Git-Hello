# l1 = [1,3,55,66,3,66,3,9,8,8]
l1 = [1,2,3,4,5,6,7,8,9,10,11]
l1.sort()
print('full list items : ',l1)
summation = sum(l1)
mean = summation / len(l1)
print('mean value : ', mean)

if len(l1) % 2 == 0:
    median = int((l1[int(len(l1)/2 - 1)] + l1[int(len(l1)/2)]) / 2)
else:
    median = l1[int(len(l1)/2)]

print('median : ',median)