x=int(input("Enter value of a: "))
y=int(input("Enter value of b: "))
opr=input("Enter ur operation: ")

def calc(x,y,opr):
    oper={"add":lambda x,y:x+y,"sub":lambda x,y:x-y,"mul":lambda x,y:x*y,"div":lambda x,y:x/y}
    return oper[opr](x,y)

b=calc(x,y,opr)
a=str(b)
w=str(x)
s=str(y)
new_path='q3.txt'
new_days=open(new_path,'w')
new_ans.write(a)
new_ans.write(x)
new_ans.write(y)
print(x,y,a)
new_a.close()
