num = int(input("num : "))
flag = True
for i in range(2, num):
  if num % i == 0 :
    flag = False
    break
if flag and num > 1:
  print("is Prime")
else:
  print("is not Prime")
