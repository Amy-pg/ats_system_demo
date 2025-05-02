import csv
import random

motivations = [
    "Web開発のスキルを活かしたいと考え応募しました。",
    "フロントエンドの技術を学びながら成長したいです。",
    "将来のキャリアアップを見据えて御社に挑戦したいです。",
    "顧客対応経験を活かして業務に貢献したいです。",
    "以前からこの職種に強い興味を持っていました。",
    "スキルアップと新しい挑戦を求めて応募しました。",
    "御社の企業理念に共感し応募しました。",
    "未経験からでも成長できる環境を求めて応募しました。",
    "社会貢献性の高い事業に関わりたいと思い応募しました。",
    "長期的に働ける環境を探していたため応募しました。"
]

statuses = ["選考中", "面接予定", "採用", "不採用"]

with open('data/applicants.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'email', 'job_id', 'message', 'apply_date', 'status', 'memo'])
    for i in range(20):
        writer.writerow([
            f"応募者{i+1}",
            f"user{i+1}@example.com",
            random.randint(1, 5),  # job_id 1～5
            random.choice(motivations),
            "2025-05-01",
            random.choice(statuses),
            ""
        ])

print("✅ applicants.csv が作成されました！")
