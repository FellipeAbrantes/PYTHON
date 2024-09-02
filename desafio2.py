n = int(input("Quantos termos quer? "))
t1 = 0
t2 = 1
count = 3
while count <= n:
    t3 = t1 + t2
    print("O número pertence a sequência de Fibonacci!", t3)
    t1 = t2
    t2 = t3
    count += 1