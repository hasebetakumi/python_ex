import csv

with open('Week6_Data/nasa_accesslog_1.csv', 'r') as f:
    read_all = csv.reader(f)
    reader = []
    for row in read_all:
        reader.append(row)
    
    # コンテンツキーを取得
    content_list = []
    for row in reader:
        content_list.append(row[1])
    content_set = set(content_list)

    # 空辞書を作成
    content_dict = {}
    for content_key in content_set:
        content_dict[content_key] = []

    # ホスト先を入れる
    for content_key in content_dict:
        for row in reader:
            if content_key == row[1]:
                content_dict[content_key].append(row[0])

# ルートパスがあれば取り除く
if '/' in content_dict:
    content_dict.pop('/')

# アクセス元ホストが100以上のコンテンツを表示
count = 0
for content_key in content_dict:
    if len(content_dict[content_key]) >= 100:
        print(content_key, len(set(content_dict[content_key])),
              len(content_dict[content_key]))
        count += 1

print(count)
