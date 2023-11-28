import random
import time

def extended_euclidean_algorithm(a, b):
    """
    Returns (gcd, x, y) such that a * x + b * y == gcd, where gcd = GCD(a, b)
    Algorithm complexity - O(log b)

    P.S. This code was taken from this URL: https://habr.com/ru/post/335906/
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse_of(n, p):
    """
    Returns m such that (n * m) % p == 1

    P.S. This code was taken from this URL: https://habr.com/ru/post/335906/
    """
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Или n равно 0, или p не является простым.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p


def generate_params(start, end):
    a = random.randint(start, end)
    b = random.randint(start, end)
    while 4 * a ** 3 + 27 * b ** 2 != 0:
        a = random.randint(start, end)
        b = random.randint(start, end)
    return a, b


def elliptic_curve(x, y, a, b, p):
    return y**2 % p == (x ** 3 + a * x + b) % p


def get_points(a, b, p):
    points = []
    for x in range(0, p):
        for y in range(0, p):
            if elliptic_curve(x, y, a, b, p):
                points.append((x, y))
    return points, len(points)


def algebraic_sum(point1, point2, a, p):
    if point1 == (0,0):
        return point2
    elif point2 == (0,0):
        return point1
    elif point1[0] == point2[0] and point1[1] != point2[1]:
        return (0,0)
    
    if point1 == point2:
        m = (3 * point1[0] ** 2 + a) * inverse_of(2 * point1[1], p)
    else:
        m = (point1[1] - point2[1]) * inverse_of(point1[0] - point2[0], p)
    
    x_r = (m ** 2 - point1[0] - point2[0]) % p
    y_r = (point2[1] + m * (x_r - point2[0])) % p
    return (x_r, -y_r % p)


def point_order(point, a, p):
    order = 0
    new_point = point
    while new_point != (0,0):
        order += 1
        new_point = algebraic_sum(point, new_point, a, p)
    return order

if __name__ == '__main__':
    a, b = generate_params(1000, 10000) # random parameters a and b
    p = 20929 # random prime number
    start = time.time()
    points, size = get_points(a, b, p)
    rand_point = points[random.randint(0, size)]
    print(f'Curve order is {size}')
    print(f'Order of point {rand_point} is {point_order(rand_point, a, p)}')
    finish = time.time()
    print(f"Time: {format(finish - start)} sec.")