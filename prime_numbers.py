def is_prime(n: int) -> bool:
    """주어진 정수 n이 소수인지 판별하는 함수"""
    if n < 2:
        return False
    # 2부터 n의 제곱근까지만 확인하면 충분합니다.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    # 1부터 100까지의 수 중 소수 찾기
    primes = [num for num in range(1, 101) if is_prime(num)]

    print(f"1부터 100 사이의 소수 ({len(primes)}개):")
    print(primes)


if __name__ == "__main__":
    main()

