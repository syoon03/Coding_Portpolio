#콘솔 계산기 프로그램
try:
    #무한반복
    while True:
        cal = input("실수 범위에서 계산하고 싶은 기호의 번호를 입력해주세요. [1.더하기/2.빼기/3.나누기/4.곱하기/5.거듭제곱/6.거듭제곱근/0.종료]: ")

        #올바른 숫자만 입력하도록 안내
        if cal not in ['1', '2', '3', '4', '5', '6', '0']:
            print("0~6 중 하나를 골라주세요.")

        #올바른 숫자 입력 시 입력받은 번호를 정수로 변환
        else:
            cal = int(cal)

            #더하기
            if cal == 1:
                num1 = float(input("첫 숫자를 입력해주세요: "))
                num2 = float(input("더할 숫자를 입력해주세요: "))
                print(f'{num1}+{num2}={num1+num2}')

            #빼기
            elif cal == 2:
                num1 = float(input("첫 숫자를 입력해주세요: "))
                num2 = float(input("뺄 숫자를 입력해주세요: "))
                print(f'{num1}-{num2}={num1-num2}')

            #나누기
            elif cal == 3:
                num1 = float(input("첫 숫자를 입력해주세요: "))
                num2 = float(input("나눌 숫자를 입력해주세요: "))
                print(f'{num1}/{num2}={num1/num2}')

            #곱하기
            elif cal == 4:
                num1 = float(input("첫 숫자를 입력해주세요: "))
                num2 = float(input("곱할 숫자를 입력해주세요: "))
                print(f'{num1}*{num2}={num1*num2}')

            #거듭제곱
            elif cal == 5:
                num1 = float(input("첫 숫자를 입력해주세요: "))
                num2 = float(input("지수를 입력해주세요: "))
                print(f'{num1}^{num2}={num1**num2}')

            #거듭제곱근
            elif cal == 6:
                num1 = float(input("첫 숫자를 입력해주세요: "))
                num2 = float(input("지수를 입력해주세요: "))

                #계산기 목적(실수 범위) 벗어나면 결과가 아니라 안내문 출력
                if num1 < 0:
                    print("계산 결과가 실수가 아닙니다.")
                else:
                    print(f'{num1}의 {num2}제곱은 {num1**(1/num2)}')

            #계산기 종료
            elif cal == 0:
                print("계산기를 종료합니다.")
                break

#숫자가 아닌 것을 입력한 경우
except ValueError:
    print("숫자가 잘못 입력되었습니다.")

#0으로 나눈 경우
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")