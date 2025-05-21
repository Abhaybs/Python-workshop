a=[[]]
b=[[]]
c=[[]]
for i in range(5):
    a[0].append(0)
for i in range(10):
    b[0].append(0)
for i in range(5):
    c[0].append(0)
section=str(input("Enter which section you want: "))
row=int(input("Enter row number: "))
column=int(input("Enter column number: "))
seat=f"{section}[{row}][{column}]"
print(seat)
if 'a' in seat:
    a[0][row]=1
elif 'b' in seat:
    b[0][row]=1
elif 'c' in seat:
    c[0][row]=1
else:
    print("choose the correct seat")
rowa="".join(str(v) for v in a[0])
rowb="".join(str(v) for v in b[0])
rowc="".join(str(v) for v in c[0])
print(f"{rowa} {rowb} {rowc}")