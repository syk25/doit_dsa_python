def bf_match(txt:str, pat: str) -> int:
    """브루트포스법으로 문자열 검색"""
    # 텍스트 0부터 끝 - 패턴의 길이까지:
        # 텍스트 상의 문자와 패턴 초기 문자의 일치 여부:
            # 다음 문자의 일치여부 검색
                # 일치하지 않으면 브레이크
            # 일치시 초기문자 인덱스 반환
    
    idx = 0
    pat_len = len(pat)
    for i in range(len(txt) - pat_len + 1):
        if txt[i:i + len(pat)] == pat:
            return i
    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요: ')
    s2 = input('패턴을 입력하세요: ')
    
    idx = bf_match(s1, s2)
    
    if idx == -1:
        print('텍스트 안에 파일이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자가 일치합니다.')
    