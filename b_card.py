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

        # 데이터 쓰기
        for row in data:
            writer.writerow(row)

    print("명함 추가 완료")


# 데이터 쓰기
write_csv(data)
