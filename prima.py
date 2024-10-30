
def next_prime(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    n += 1  
    while not is_prime(n):
        n += 1
    return n
n = int(input("Masukkan bilangan: "))
print("Bilangan prima setelah", n, "adalah", next_prime(n))

