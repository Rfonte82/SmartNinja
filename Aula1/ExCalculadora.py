
a = float(input("inserir a="))
b = float(input("inserir b="))
operation = str(input("operation"))

if operation== "+":
    print( "resultado ="+ str(a+b))
elif operation== "-":
    print( "resultado ="+ str(a-b))
elif operation== "*":
    print( "resultado ="+ str(a*b))
elif operation == "/":
    print( "resultado ="+ str(a/b))
else:
    print("erro")

