
# I am not good at math and had to do a lot of research for this
# I asked my girlfriend and chatgpt for math help and I think you are asking for
# Leibniz formula for π


def alternating_sum(n):
    """
    """
    total = 0
    for k in range(1, n+1):
        term = ((-1)**(k+1)) / (2*k-1)
        total += term
    return total * 4


print(alternating_sum(10000000))
