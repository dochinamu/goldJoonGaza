Str = input()
PlusCal = list()
MinusCal = list()
a=0
b = 0
for i in range(len(Str)):
    if Str[i] == '+' or Str[i] == '-':
        if a == 0:
            PlusCal.append(int(Str[:i]))
        else:
            PlusCal.append(int(Str[a+1:i]))
        if Str[i] == '+':
            pass
        else :
            b=0
            for c in range(len(PlusCal)):
                b = b+PlusCal[c]
            PlusCal = list()
            MinusCal.append(b)

        a = i
    if i+1==len(Str):
        if a==0:
            MinusCal.append(int(Str))    
        else:   
            b=0
            PlusCal.append(int(Str[a+1:i+1]))
            for c in range(len(PlusCal)):
                b = b+PlusCal[c]
            MinusCal.append(b)

Goal = MinusCal[0]
for d in range(1,len(MinusCal)):
    Goal=Goal-MinusCal[d]
print(Goal)