# 실습문제 4)

study_hour = int(input("공부시간을 입력하세요(시간) >>>"))

if study_hour >= 10:
    print("휴대폰 잠금이 해제 됩니다.")
elif study_hour >= 5:
    print("휴대폰 30분간 사용가능 합니다.")
else:
    print("휴대폰 사용이 불가능 합니다.")