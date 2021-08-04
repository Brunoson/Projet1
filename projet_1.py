def fibonaci(n):
    i,j=0,1
    fib=[]
    while i<n:
        fib.append(i)
        i,j=j,i+j
    return fib

def trier(classeur, nombre):
    if nombre>0:
        classeur["positif"].append(nombre)
    else:
        classeur["negatif"].append(nombre)
    return classeur