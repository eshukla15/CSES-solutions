from collections import Counter
s = input()
c = 0
st = Counter(s)
flag = False
s1, s2 = "", ""
for i in st.values():
    if i%2 == 1 :
        if c==1:
            print("NO SOLUTION")
            flag = True
            break
        c+=1
if not flag:
    t = ""
    for c, i in st.items():
        if i%2 == 0:
            s1 += (c*(i//2))
            s2 = (c*(i//2))+s2
        else:
            t = i*c
    print(s1+t+s2)