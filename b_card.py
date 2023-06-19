import csv

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

def show_data():
    # 데이터 목록 보기
    print("===== 데이터 목록 =====")
    rows = read_csv()
    for row in rows:
        print(row)

def add_data():
    name = input("이름을 입력하세요: ")
    company = input("소속을 입력하세요: ")
    job = input("직업을 입력하세요: ")
    data = [name, company, job]
    
    rows = read_csv()
    rows.append(data)
    
    # CSV 파일 다시 쓰기
    write_csv(rows)
    print("데이터 추가 완료")

def delete_data():
    # 데이터 목록 보기
    show_data()

    name = input("삭제할 데이터의 이름을 입력하세요: ")

    rows = read_csv()
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

# 데이터 목록 보기
show_data()

while True:
    add_choice = input("데이터를 추가하시겠습니까? (Y/N): ")
    if add_choice.upper() == 'Y':
        add_data()
        break
    elif add_choice.upper() == 'N':
        break
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")

while True:
    delete_choice = input("데이터를 삭제하시겠습니까? (Y/N): ")
    if delete_choice.upper() == 'Y':
        delete_data()
        break
    elif delete_choice.upper() == 'N':
        break
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")
