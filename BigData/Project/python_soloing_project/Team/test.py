import random
import json
from collections import defaultdict

# 팀원 이름 목록
people = [
    "박란영", "조혜리", "전민규", "안효준", "김경태", "김태헌", "구성윤", "황은혁",
    "김경환", "곽경민", "김재성", "도영훈", "한세진", "이민하", "장재웅", "이현종",
    "박형준", "손지원", "황지원", "김환선", "김민석", "이동건", "김영주", "안윤호",
    "김미소", "김아란", "김도연", "권도운", "김이현", "김현주", "이송은", "박지훈"
]

# 파일 이름 설정
filename = 'team_history.json'

# 팀 구성 함수
def create_teams(people, history):
    # 사람들 간의 중복 횟수 계산
    counts = defaultdict(int)
    for round_teams in history:
        for team in round_teams:
            for i in range(len(team)):
                for j in range(i + 1, len(team)):
                    counts[(team[i], team[j])] += 1
                    counts[(team[j], team[i])] += 1
    
    # 최소 중복 횟수를 가지는 팀 구성
    best_teams = None
    min_repeat = float('inf')
    
    for _ in range(1000):  # 여러 번 시도하여 최적의 팀 구성 찾기
        random.shuffle(people)
        teams = [people[i:i + 4] for i in range(0, len(people), 4)]
        
        repeat_count = sum(counts[(min(team[i], team[j]), max(team[i], team[j]))] for team in teams for i in range(len(team)) for j in range(i + 1, len(team)))
        
        if repeat_count < min_repeat:
            min_repeat = repeat_count
            best_teams = teams
            
    return best_teams

# 팀 내역을 파일에 저장하는 함수
def save_teams(filename, all_rounds):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_rounds, f, ensure_ascii=False, indent=4)

# 파일에서 팀 내역을 불러오는 함수
def load_teams(filename):
    encodings = ['utf-8', 'cp949', 'euc-kr']  # 시도할 인코딩 리스트
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as f:
                all_rounds = json.load(f)
            return all_rounds
        except (UnicodeDecodeError, FileNotFoundError):
            continue  # 인코딩이 맞지 않거나 파일이 없으면 다음 인코딩 시도
    return []  # 파일을 읽지 못하면 빈 리스트 반환

# 팀 내역에 새로운 라운드 추가 함수
def add_round(all_rounds, new_round):
    all_rounds.append(new_round)
    return all_rounds

# 특정 라운드를 삭제하는 함수
def delete_round(all_rounds, round_number):
    if 0 <= round_number < len(all_rounds):
        del all_rounds[round_number]
    return all_rounds

# 메인 실행 부분
def main():
    all_rounds = load_teams(filename)

    # 새로운 라운드 추가
    new_round = create_teams(people, all_rounds)
    all_rounds = add_round(all_rounds, new_round)
    save_teams(filename, all_rounds)
    
    # 특정 라운드 삭제 (예: 0번째 라운드 삭제)
    round_to_delete = 7
    all_rounds = delete_round(all_rounds, round_to_delete)
    save_teams(filename, all_rounds)
    round_to_delete = 6
    all_rounds = delete_round(all_rounds, round_to_delete)
    save_teams(filename, all_rounds)
    round_to_delete = 5
    all_rounds = delete_round(all_rounds, round_to_delete)
    save_teams(filename, all_rounds)
    round_to_delete = 4
    all_rounds = delete_round(all_rounds, round_to_delete)
    save_teams(filename, all_rounds)
    
    # 결과 출력
    for i, round_teams in enumerate(all_rounds, 1):
        print(f'Round {i}:')
        for team in round_teams:
            print(team)
        print()  # 각 라운드 사이에 빈 줄 추가

if __name__ == "__main__":
    main()


    """
    delete_round 함수: 주어진 round_number에 해당하는 라운드를 삭제합니다.
삭제된 내역 저장: 삭제 후 업데이트된 내역을 파일에 다시 저장합니다.
"""