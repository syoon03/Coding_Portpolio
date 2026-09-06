import sys

#몸무게(kg)와 키(cm)를 입력받아 float으로 변환
try:
    weight_kg = float(input("몸무게(kg): "))
    height_cm = float(input("키(cm): "))
except ValueError:
    #숫자가 아닌 값을 입력한 경우 종료
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    sys.exit()
else:
    #음수나 0을 입력한 경우 방어 후 종료
    if weight_kg <= 0 or height_cm <= 0:
        print("양수를 입력해주세요. 프로그램을 종료합니다.")
        sys.exit()
    else:
        #키를 cm에서 m로 변환하여 BMI 계산
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        #BMI 값에 따라 등급 분류
        if bmi < 18.5:
            bmi_category = "저체중"
        elif bmi <= 22.9:
            bmi_category = "정상"
        elif bmi <= 24.9:
            bmi_category = "과체중"
        elif bmi <= 29.9:
            bmi_category = "비만 1단계"
        elif bmi <= 34.9:
            bmi_category = "비만 2단계"
        else:
            bmi_category = "비만 3단계"

        #최종 BMI 수치와 등급 출력
        print(f"BMI: {bmi:.2f}")
        print(f"당신은 {bmi_category}입니다.")