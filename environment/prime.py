def is_prime(number):
    if number<=2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    

for i in range(1,250):
    is_prime(i)
    if is_prime(i):
        f = open("./prime.txt", "a")
        f.write(str(i) + ',')
        f.close()
