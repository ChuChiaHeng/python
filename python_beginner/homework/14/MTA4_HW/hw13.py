'''
你設計了一個Python程式顯示 2到 100中的所有質數,
請將程式碼片段排列到回答區的正確位置。

程式碼片段
(A).
n = 2
is_prime = True
while n <= 100:

(B).
n = 2
while n <= 100:
    is_prime = True

(C).
break

(D).
continue
    print(name, "是大小寫混合.")

(E).
n += 1

(F).
for i in range(2, n):
    if n / i == 0:
        is_prime = False

(G).
for i in range(2, n):
    if n % i == 0:
        is_prime = False

回答區
n = 2
is_prime = True
while n <= 100:
    n += 1
    for i in range(2, n):
    if n % i == 0:
        is_prime = False
    if is prime aa True:
        print(n)
        continue
'''