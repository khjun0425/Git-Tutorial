def gugudan(a,b):
  for i in range(9):
    for j in range(4):
      if len(str((i + 1)*a)) == 1:
        print(a,'X',(i+1),'= ',(i+1)*a,end='    ')
      else:
        print(a,'X',(i+1),'=',(i+1)*a,end='    ')
      a = a + 1
    a = a - 4
    print(end='\n')
gugudan(2,5)
print('\n')
gugudan(6,9)
