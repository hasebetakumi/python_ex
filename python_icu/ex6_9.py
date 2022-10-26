
with open('Week6_Data/scorelist.txt', 'r') as file:
    reader = file.readlines()
    # 卒業年キーを取得
    grad_year_list = []
    for row in reader:
        grad_year_list.append(row[0:2])
    grad_year_set = set(grad_year_list)

    # 空辞書を生成
    grad_dict = {}
    for grad_key in grad_year_set:
        grad_dict[grad_key] = []

    # 学籍番号を入れる
    for grad_key in grad_dict:
        for row in reader:
            if grad_key == row[0:2]:
                grad_dict[grad_key].append(row[0:6])

# キーが卒業年、値が学生番号の辞書
print(grad_dict)
for grad_key in grad_dict:
    print(grad_key, len(grad_dict[grad_key]))   

