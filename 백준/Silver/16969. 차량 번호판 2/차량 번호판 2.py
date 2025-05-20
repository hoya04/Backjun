MOD = 1000000009  # 나머지 연산에 사용할 상수

def count_license_plates(pattern):
    """
    입력된 패턴에 따라 가능한 번호판의 개수를 계산합니다.
    
    Args:
        pattern (str): 번호판 패턴 ('c'는 알파벳, 'd'는 숫자)
    
    Returns:
        int: 가능한 번호판의 총 개수를 1,000,000,009로 나눈 나머지
    """
    # 첫 문자에 대한 경우의 수 초기화
    if pattern[0] == 'd':
        result = 10  # 숫자는 10가지 (0-9)
    else:  # pattern[0] == 'c'
        result = 26  # 알파벳은 26가지 (a-z)
    
    # 두 번째 문자부터 순회하며 계산
    for i in range(1, len(pattern)):
        current = pattern[i]
        previous = pattern[i-1]
        
        if current == 'd':  # 현재 위치가 숫자
            if current == previous:  # 이전 위치도 숫자였다면
                result = (result * 9) % MOD  # 이전과 다른 숫자만 가능 (10-1=9)
            else:
                result = (result * 10) % MOD  # 모든 숫자 가능
        else:  # current == 'c', 현재 위치가 알파벳
            if current == previous:  # 이전 위치도 알파벳이었다면
                result = (result * 25) % MOD  # 이전과 다른 알파벳만 가능 (26-1=25)
            else:
                result = (result * 26) % MOD  # 모든 알파벳 가능
    
    return result

# 입력 처리 및 결과 출력
pattern = input().strip()
answer = count_license_plates(pattern)
print(answer)