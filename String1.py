s=input("Enter A String : ")

uc=0
lc=0
al=0
nm=0
sp=0

for i in s:
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1

print("Total Upper Case : ",uc)
print("Total Lower Case : ",lc)
print("Total Alphabets : ",al)
print("Total Numericals : ",nm)
print("Total Space : ",sp)
