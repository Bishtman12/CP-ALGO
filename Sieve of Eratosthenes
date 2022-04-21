# Prime Factor determination Algorithm
#pre-computing an array which marks if it is a prime or not
def generate_sieve_array(n):
    A = [-1]*(n+1)
    A[0] = 0
    A[1] = 0
    for i in range(2,n+1):
        if A[i] == -1: #marked as non-prime till now
            A[i] = 1
            j = i*i
            while j<n+1:
                A[j] = 0
                j +=i
    return A
def check_prime(n):
    A = generate_sieve_array(n)
    return A[n]==1
print(check_prime(17))
