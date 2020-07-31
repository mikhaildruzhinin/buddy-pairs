import argparse

parser = argparse.ArgumentParser(description='buddy pair')
parser.add_argument('start', type=int, help='start')
parser.add_argument('limit', type=int, help='limit')

args = parser.parse_args()


def get_divisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors


def buddy(start, limit):
    for n in range(start, limit + 1):
        n_divisors = get_divisors(n)
        m = sum(n_divisors) - 1
        if m <= n:
            continue
        m_divisors = get_divisors(m)
        if sum(m_divisors) == n + 1:
            return [n, m]
    return 'Nothing'


def main():
    result = buddy(args.start, args.limit)
    print(result)

if __name__ == '__main__':
    main()
