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
        writer.writerows(data)  # Write all rows at once using writerows

def read_csv():
    # CSV 파일 읽기
    with open("data.csv", mode="r") as file:
        # CSV reader 생성
        reader = csv.reader(file)
        rows = list(reader)
    return rows

def delete_data(name):
    # 데이터 목록 보기
    print("===== 데이터 목록 =====")
    rows = read_csv()
    for row in rows:
        print(row)

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
        print(f"\n{name}의 데이터 삭제 완료")
    else:
        print(f"\n{name}의 데이터를 찾을 수 없습니다.")

# 데이터 쓰기
write_csv(data)

# 데이터 목록 보기 및 삭제
delete_data("하은서")
