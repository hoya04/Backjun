def reconstruct_line(n, taller_counts):
    """
    사람들의 키 순서를 재구성하는 함수.

    :param n: 총 사람 수 (1번부터 n번까지 사람 존재)
    :param taller_counts: 각 사람이 자신보다 키 큰 사람이 앞에 몇 명 있는지 나타낸 리스트
    :return: 줄을 선 최종 순서가 담긴 리스트
    """
    line = [0] * n  # 줄을 설 배열, 0은 아직 비어있음을 의미

    # 사람 번호는 1번부터 시작
    for person in range(1, n + 1):
        taller_in_front = taller_counts[person - 1]  # 해당 사람 앞에 있어야 할 더 큰 사람 수
        count = 0  # 현재까지 만난 빈 자리 수

        # 줄에서 적절한 위치 찾기
        for i in range(n):
            if line[i] == 0:  # 빈 자리를 찾았을 때만 카운트
                if count == taller_in_front:
                    line[i] = person  # 조건이 만족되면 그 자리에 사람을 세움
                    break
                count += 1  # 조건 불만족 시 계속 진행

    return line  # 완성된 줄 반환

def main():
    # 입력 처리
    n = int(input())  # 사람 수 입력
    taller_counts = list(map(int, input().split()))  # 각 사람의 '앞에 있어야 할 더 큰 사람 수' 입력

    # 줄 재구성 함수 호출
    result = reconstruct_line(n, taller_counts)

    # 출력
    print(' '.join(map(str, result)))

# 스크립트 실행 시작점
if __name__ == "__main__":
    main()