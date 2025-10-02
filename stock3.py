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
    date_str = input("輸入日期 (YYYY-MM-DD): ")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("日期格式錯誤，請使用 YYYY-MM-DD")
        return

    possible_owners = ["我", "蔡坤林"]
    selected_owners = []

    print("請選擇投入持有人（可多選，輸入對應數字，輸入空白結束）:")
    for i, owner in enumerate(possible_owners, 1):
        print(f"{i}. {owner}")

    while True:
        choice = input("選擇持有人編號 (或空白結束): ").strip()
        if choice == "":
            break
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(possible_owners):
                owner = possible_owners[idx - 1]
                if owner not in selected_owners:
                    selected_owners.append(owner)
                else:
                    print(f"{owner} 已選擇過")
            else:
                print("輸入的編號不在範圍內")
        else:
            print("請輸入數字編號或空白")

    if not selected_owners:
        print("至少要選擇一位持有人")
        return

    owners_amounts = {}
    for owner in selected_owners:
        while True:
            try:
                amount = float(input(f"請輸入 {owner} 的投入金額: "))
                if amount < 0:
                    print("金額不可為負數")
                else:
                    break
            except ValueError:
                print("請輸入數字")
        owners_amounts[owner] = amount

    total_amount = sum(owners_amounts.values())
    if total_amount <= 0:
        print("總投入金額需大於 0")
        return

    record = {
        "stock_name": stock_name,
        "date": date_str,
        "owners": owners_amounts,
        "total_amount": total_amount
    }
    records.append(record)
    print("紀錄已新增")

def show_records(records):
    if not records:
        print("目前沒有紀錄")
        return
    print("\n股票定期定額紀錄:")
    for idx, rec in enumerate(records, 1):
        owners_str = ", ".join([f"{k}: {v}" for k, v in rec["owners"].items()])
        print(f"{idx}. 股票名稱: {rec['stock_name']}, 日期: {rec['date']}, 總金額: {rec['total_amount']}, 持有人投入: {owners_str}")

def stats_by_owner(records):
    stats = {}
    for rec in records:
        for owner, amount in rec["owners"].items():
            stats[owner] = stats.get(owner, 0) + amount
    if not stats:
        print("沒有資料可供統計")
        return
    print("\n按持有人統計投入總金額:")
    for owner, total in stats.items():
        print(f"{owner}: {total}")

def stats_by_stock(records):
    stats = {}
    for rec in records:
        stock = rec["stock_name"]
        stats[stock] = stats.get(stock, 0) + rec["total_amount"]
    if not stats:
        print("沒有資料可供統計")
        return
    print("\n按股票名稱統計投入總金額:")
    for stock, total in stats.items():
        print(f"{stock}: {total}")

def main():
    print("程式執行目錄：", os.getcwd())
    records = load_records()

    while True:
        print("\n股票定期定額記帳")
        print("1. 新增紀錄")
        print("2. 顯示所有紀錄")
        print("3. 按持有人統計投入總金額")
        print("4. 按股票名稱統計投入總金額")
        print("5. 離開")

        choice = input("請選擇功能 (1-5): ")
        if choice == "1":
            add_record(records)
            save_records(records)
        elif choice == "2":
            show_records(records)
        elif choice == "3":
            stats_by_owner(records)
        elif choice == "4":
            stats_by_stock(records)
        elif choice == "5":
            print("再見！")
            break
        else:
            print("選項錯誤，請重新輸入")

if __name__ == "__main__":
    main()
