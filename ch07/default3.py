
def connect_db(host="localhost", port=3306, timeout=3):
    print(host, port, timeout)

connect_db()    # 기본 연결 수행
connect_db(timeout=10)

# 아이디어 구상
# 문서화
# 데이터베이스(db) : 데이터 집합

# DB에 접근하고 싶다.
# DB는 같은 네트워크에 내 컴퓨터로 제어되고 있어 => 접근방법
# DB에 데이터를 꺼내오려면 port를 통해서 가져와야해.
# 시스템에 접속해서 3초 기다렸다가 안되면 재접속 해야지.

