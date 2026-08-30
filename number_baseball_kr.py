import random

DIGIT_COUNT = 3

def generate_answer():
    #0~9 중 중복 없는 DIGIT_COUNT개의 숫자를 무작위로 골라 정답으로 반환
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:DIGIT_COUNT]

def judge(answer, guess):
    #정답과 추측을 비교해 (스트라이크, 볼) 개수를 반환
    strike = 0
    ball = 0
    for i in range(DIGIT_COUNT):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1
    return strike, ball

def get_valid_guess():
   #조건(자릿수·중복없음·숫자만)을 만족하는 입력이 나올 때까지 반복해서 입력
    while True:
        raw = input(f"숫자 {DIGIT_COUNT}개를 입력하세요: ")

        if not raw.isdigit():
            print("숫자만 입력해주세요.")
            continue

        if len(raw) != DIGIT_COUNT:
            print(f"{DIGIT_COUNT}자리 숫자를 입력해주세요.")
            continue

        guess = list(map(int, raw))

        if len(set(guess)) != DIGIT_COUNT:
            print("중복되지 않는 숫자를 입력해주세요.")
            continue

        return guess

def play_game():
   #숫자야구 게임을 시작해 정답을 맞힐 때까지 반복 진행
    answer = generate_answer()
    count = 0
    while True:
        guess = get_valid_guess()
        count += 1
        strike, ball = judge(answer, guess)
        print(f"{strike} 스트라이크, {ball} 볼")
        print(f"현재 시도 횟수: {count}")
        if strike == DIGIT_COUNT:
            print(f"정답입니다! 총 {count}번 시도했습니다.")
            break

if __name__ == "__main__":
    play_game()