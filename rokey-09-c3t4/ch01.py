# ch01.py

# Rokey 9기 3반 4조 1주차 스터디

# 코드를 몇일 전으로 되돌리려면
# 1. 매일 백업
# 2. 버전관리 소프트웨어 사용

# git을 사용하면 작업한 코드를 기록, 보관 가능
# 과거시점으로 돌아가거나, 작업내용 열람 가능

# git 과 gitHub 차이
# git은 인터넷 필요없이 컴퓨터 내부에서 작동하는 버전 관리 시스템
# 언제든지, 과거에 저장해둔 시점으로 되돌릴 수 있음

# gitHub는 git으로 관리하는 프로젝트들을 온라인에 올릴 수 있는 클라우드 저장소 서비스
# 인터넷상에 코드를 백업하고 관리
# 여러사람이 동시에 하나의 프로젝트에 참여할때, 각자의 코드를 합치거나 리뷰할 수 있음

# git 다운로드
# 1. 구글에 Git 공홈에서 다운로드
# 2. 다른 설정은 디폴트값을 설정하지만, 
#     Editor 선택은 vim이 아니라 'Use Visual Studio Code as Git's default editor'로 선택
#     "Adjusting the name of the initial branch" 단계에서 Override the default branch name for new repositories를 선택
# 3. 터미널에서 사용자 이름과 이메일 설정
# git config --global user.name "본인이름"
# git config --global user.email "본인이메일@example.com"
# 4. 'git config --list' 로 등록 확인

# GitHub에 파일 올리는법
# 1. GitHub 우측 상단의 프로필 클릭
# 2. New repository를 눌러서 새로운 repository 생성
# 3. 화면에 나타나는 HTTPS 주소 복사
# 4. 터미널에 'git init' 명령어 입력
# 5. 'git add .' 명령어로 파일 준비
# 6. git monnit -m "First Commit" 명령어로 세이브 포인트 생성(m 뒤에는 코멘트같은거)
# 7. 'git remote add origin 복사한주소'를 입력하여 원격 저장소 연결
# 8. 'git branch -M main' 브랜치 이름 설정?
# 9. 'git push -u origin main' 명령어로 최종 업로드
