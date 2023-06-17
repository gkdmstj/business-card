import csv

# CSV 파일에 저장할 데이터
data = [
    ["이름", "소속", "직업"],
    ["홍길동", "삼성", "개발자"],
    ["신짱구", "엘지", "UI&UX디자이너"],
    ["하은서", "스타벅스", "MD디자이너"],
    ["흰둥이", "카카오", "CEO"]
]

def write_csv(data):
    # CSV 파일 열기
    with open("data.csv", mode="w", newline="") as file:
        # CSV writer 생성
        writer = csv.writer(file)
      
def delete_data(name):
    # CSV 파일 읽기
    with open("data.csv", mode="r") as file:
        # CSV reader 생성
        reader = csv.reader(file)
        rows = list(reader)

    # 데이터 삭제
    deleted = False
    for row in rows:
        if row[0] == name:
            rows.remove(row)
            deleted = True
            break

    if deleted:
        # CSV 파일 다시 쓰기
        write_csv(rows)
        print(f"{name}의 데이터 삭제 완료")
    else:
        print(f"{name}의 데이터를 찾을 수 없습니다.")

# 데이터 쓰기
write_csv(data)

# 데이터 삭제
delete_data("기철이")