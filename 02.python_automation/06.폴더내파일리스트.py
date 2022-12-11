import os

# 현재 폴더 내 모든 파일 출력
file_list = os.listdir('C:/Users/mynam/Downloads')
print(file_list)

# 반복문을 통해 각 파일 확장자 확인한다.
for file in file_list:
    name,ext = os.path.splitext(file)
    