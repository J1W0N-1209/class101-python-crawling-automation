import os 

# 상대 경로
# os.mkdir('테스트1')

# 상대 경로 이용 2
# os.mkdir('02.python_automation/테스트2')

# 절대 경로 이용
# os.mkdir('c:/startcoding/테스트3') # 맥 user/documents/startcoding/테스트3

# 절대 경로 찾기
os.mkdir('C:/Users/mynam/Downloads/images') # 맥 

# 폴더가 없을 때만 만들기
if not os.path.exists('C:/Users/mynam/Downloads/images'):
    os.mkdir('C:/Users/mynam/Downloads/images')