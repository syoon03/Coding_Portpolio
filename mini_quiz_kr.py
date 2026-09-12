import random as rd

questions = [
    {
        "question": "대한민국의 수도는?",
        "choices": ["서울", "부산", "인천", "경주"],
        "answer": 0
    },
    {
        "question": "미국의 수도는?",
        "choices": ["워싱턴 D.C", "뉴욕", "시카고", "보스턴"],
        "answer": 0
    },
    {
        "question": "중국의 수도는?",
        "choices": ["난징", "상하이", "베이징", "선전"],
        "answer": 2
    },
    {
        "question": "이탈리아의 수도는?",
        "choices": ["나폴리", "밀라노", "로마", "피렌체"],
        "answer": 2
    },
    {
        "question": "스페인의 수도는?",
        "choices": ["세비야", "바르셀로나", "발렌시아", "마드리드"],
        "answer": 3
    },
]


def ask_question(question_data, number):
    #문제 하나를 출력하고, 사용자 입력을 받아 정답 여부(True/False)를 반환한다.
    print(f"\n[문제 {number}] {question_data['question']}")

    num_choices = len(question_data["choices"])
    for i, choice in enumerate(question_data["choices"], start=1):
        print(f"  {i}. {choice}")

    while True:
        user_input = input("정답 번호를 입력하세요: ")

        try:
            user_answer_index = int(user_input) - 1
        except ValueError:
            print(f"숫자로만 입력해주세요. (1~{num_choices} 중 하나)")
            continue

        if user_answer_index < 0 or user_answer_index >= num_choices:
            print(f"1~{num_choices} 사이의 번호를 입력해주세요.")
            continue

        break

    return user_answer_index == question_data["answer"]


def print_grade(score):
    #최종 점수(5점 만점)에 따라 등급 메시지를 출력
    if score == 5:
        print("완벽합니다!")
    elif score == 4:
        print("훌륭해요!")
    elif score == 3:
        print("좋아요.")
    elif score == 2:
        print("아쉬워요.")
    elif score == 1:
        print("노력해봐요.")
    else:
        print("다시 해볼까요?")


def run_quiz(question_list):
    #문제은행을 랜덤한 순서로 출제하고, 최종 점수와 등급을 출력
    score = 0
    shuffled_questions = question_list[:]
    rd.shuffle(shuffled_questions)

    for index, question_data in enumerate(shuffled_questions, start=1):
        is_correct = ask_question(question_data, index)

        if is_correct:
            print("정답입니다!")
            score += 1
        else:
            correct_choice = question_data["choices"][question_data["answer"]]
            print(f"오답입니다. 정답은 '{correct_choice}' 입니다.")

    print_grade(score)
    print(f"총 {len(question_list)}문제 중 {score}개 정답입니다.")


if __name__ == "__main__":
    run_quiz(questions)