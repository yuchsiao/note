



# If b > a, it will becomes gcd(b, a) in the next round
# Default behavior of modulo a % b:
#   sign goes with b
# Hence, 
# If b < 0, then a % b <= 0, so gcd <= 0
# If b > 0, then a % b >= 0, so gcd >= 0
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
