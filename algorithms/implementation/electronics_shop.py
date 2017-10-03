money = [int(i) for i in input().split(' ')][0]
kbp = [int(i) for i in input().split(' ')]
usbp = [int(i) for i in input().split(' ')]
print(max([i+j if i+j<=money else -1 for i in kbp for j in usbp])