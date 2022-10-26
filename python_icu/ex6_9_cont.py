from statistics import mean
import numpy as np

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

    # 得点を入れる
    for grad_key in grad_dict:
        for row in reader:
            if grad_key == row[0:2]:
                grad_dict[grad_key].append(row[7:9])

# 各卒業年の平均
grad_score_mean = {}
for grad_key in grad_dict:
    # 数値に変換（numpy配列にしてint型へ）
    grad_score_np = np.int_(grad_dict[grad_key])
    # list型に戻す
    grad_score_list = list(grad_score_np)

    grad_score_mean[grad_key] = mean(grad_score_list)

print(grad_score_mean)
