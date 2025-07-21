from basics_maths import *

# --------- Prime Number Tests ---------

def test_basic_primes():
    
    assert checkPrime(2) == True
    assert checkPrime(3) == True
    assert checkPrime(5) == True
    assert checkPrime(7) == True

def test_basic_composites():
    assert checkPrime(4) == False
    assert checkPrime(6) == False
    assert checkPrime(9) == False
    assert checkPrime(15) == False

def test_edge_cases():
    assert checkPrime(0) == False
    assert checkPrime(1) == False
    assert checkPrime(-7) == False

def test_large_numbers():
    assert checkPrime(97) == True
    assert checkPrime(9973) == True
    assert checkPrime(100) == False
    assert checkPrime(10007) == True

def test_even_numbers_except_2():
    for n in range(4, 100, 2):
        assert checkPrime(n) == False

# --------- Armstrong Number Tests ---------

def test_armstrong_basic():
    assert isArmstrong(0) == True
    assert isArmstrong(1) == True
    assert isArmstrong(153) == True
    assert isArmstrong(370) == True
    assert isArmstrong(371) == True
    assert isArmstrong(407) == True

def test_armstrong_false_cases():
    assert isArmstrong(100) == False
    assert isArmstrong(200) == False
    assert isArmstrong(154) == False

def test_armstrong_large_numbers():
    assert isArmstrong(9474) == True
    assert isArmstrong(9475) == False
    assert isArmstrong(9926315) == True  # 7-digit Armstrong

def test_armstrong_negative_and_edge():
    assert isArmstrong(-153) == False
    assert isArmstrong(-1) == False

# --------- GCD Tests ---------

def test_gcd_normal_cases():
    assert gcd(9, 12) == 3
    assert gcd(10, 5) == 5
    assert gcd(100, 10) == 10
    assert gcd(81, 27) == 27

def test_gcd_zero_cases():
    assert gcd(0, 10) == 10
    assert gcd(10, 0) == 10
    assert gcd(0, 0) == 0  # Depends on your definition

def test_gcd_same_numbers():
    assert gcd(7, 7) == 7
    assert gcd(100, 100) == 100

def test_gcd_coprime():
    assert gcd(13, 17) == 1
    assert gcd(35, 64) == 1

def test_gcd_large_numbers():
    assert gcd(123456, 7890) == 6
    assert gcd(987654321, 123456789) == 9

def test_gcd_negative_inputs():
    assert gcd(-25, -5) == 5
    assert gcd(-10, 15) == 5
    assert gcd(10, -15) == 5