import json
from datetime import datetime
import os

FILENAME = "stock_records.json"

def load_records():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_records(records):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

def add_record(records):
    stock_name = input("輸入股票名稱: ")
    amount = float(input("輸入定期定額金額: "))
    date_str = input("輸入日期 (YYYY-MM-DD): ")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("日期格式錯誤，請使用 YYYY-MM-DD")
        return

    print("選擇持有人：")
    print("1. 我")
    print("2. 我和蔡坤林")
    owner_choice = input("請輸入選項 (1 或 2): ")
    if owner_choice == "1":
        owner = "我"
    elif owner_choice == "2":
        owner = "我和蔡坤林"
    else:
        print("選項錯誤，預設為「我」")
        owner = "我"

    record = {
        "stock_name": stock_name,
        "amount": amount,
        "date": date_str,
        "owner": owner
    }
    records.append(record)
    print("紀錄已新增")

def show_records(records):
    if not records:
        print("目前沒有紀錄")
        return
    print("\n股票定期定額紀錄:")
    for idx, rec in enumerate(records, 1):
        print(f"{idx}. 股票名稱: {rec['stock_name']}, 金額: {rec['amount']}, 日期: {rec['date']}, 持有人: {rec.get('owner', '未知')}")

def main():
    print("程式執行目錄：", os.getcwd())
    records = load_records()

    while True:
        print("\n股票定期定額記帳")
        print("1. 新增紀錄")
        print("2. 顯示所有紀錄")
        print("3. 離開")

        choice = input("請選擇功能 (1-3): ")
        if choice == "1":
            add_record(records)
            save_records(records)
        elif choice == "2":
            show_records(records)
        elif choice == "3":
            print("再見！")
            break
        else:
            print("選項錯誤，請重新輸入")

if __name__ == "__main__":
    main()
