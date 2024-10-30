def sum_of_primes(start, end):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    
    
    prime_sum = sum(primes)
    primes_str = '+'.join(map(str, primes))
    print(f"{primes_str} = {prime_sum}")
    return prime_sum

start = int(input("Masukkan angka awal: "))
end = int(input("Masukkan angka akhir: "))
sum_of_primes(start, end)
