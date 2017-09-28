# coding: utf-8
""" SOMによるノイズ除去を行う """

import pandas as pd
import numpy as np

# 定数を定義
MAX_LEARN = 1000000 # 学習回数
NUM_REP = 6         # 実験の試行回数
ALPHA_INIT = 0.5    # 学習率係数の初期値
DELTA_INIT = 0.2    #
SOM_MAP_UNIT = 100   # マッピング層のユニット数
SOM_IN_UNIT = 5     # 入力層のユニット数
RAND_MAX = 32767

# クラスを定義
class NeighboringArea():
    """ 近傍領域の範囲を記録するクラス """
    def __init__(self):
        self.min = 0
        self.max = 0

class MappingLayer():
    """ マッピング層の結合荷重を記録するクラス """
    def __init__(self):
        self.weight = np.zeros(SOM_IN_UNIT)
        self.category = ""

class SomData():
    def __init__(self):
        self.input_data = np.zeros(SOM_IN_UNIT)
        self.winner_unit = 0
        self.map_l = []

        for i in range(SOM_MAP_UNIT):
            self.map_l.append(MappingLayer())

data = pd.read_csv(
    'C:/Users/ROBO-E-03/Desktop/scope/data/sensor.csv') # データの読み込み
num_lines = sum(1 for line in open(
    "C:/Users/ROBO-E-03/Desktop/scope/data/sensor.csv")) - 1 # データ数
np.random.seed(seed=1) # 乱数のシードを初期化

def som_main():
    """ メイン関数 """
    som = SomData()
    nei_a = NeighboringArea()

    som_initialize(som)
    som_learn(nei_a, som)
    result = som_test(som)

    print(result)

def som_initialize(som):
    """ 入力層とマッピング層の結合荷重を初期化 """
    for i in range(SOM_MAP_UNIT):
        for j in range(SOM_IN_UNIT):
            som.map_l[i].weight[j] = np.random.randint(RAND_MAX) / RAND_MAX * \
                                     2.5 + 1.25

def som_learn(nei_a, som):
    """ 学習フェーズ """
    for t in range(MAX_LEARN):
        # p1 = np.random.randint(NUM_REP - 1)
        p2 = np.random.randint(num_lines)

        for i in range(SOM_IN_UNIT):
            num_ch = i + 1
            ch = "ch" + str(num_ch)

            som.input_data[i] = data[ch][p2]

        # 勝者ユニットの探索
        som_win_unit(som)

        # 近傍領域の算出
        span = 3 * SOM_MAP_UNIT / 8
        span = int(span * 1.0 - t / MAX_LEARN + 0.5)
        nei_a.min = 0 if som.winner_unit - span < 0 else som.winner_unit - span
        nei_a.max = SOM_MAP_UNIT - 1 if som.winner_unit + span > \
                    SOM_MAP_UNIT - 1 else som.winner_unit + span

        # 学習率係数の更新
        alpha = ALPHA_INIT * (1.0 - t / MAX_LEARN)

        # 結合荷重の更新
        for i in range(nei_a.min, nei_a.max + 1):
            for j in range(SOM_IN_UNIT):
                som.map_l[i].weight[j] += alpha * (som.input_data[j] -
                                                   som.map_l[i].weight[j])

        # if t % 100000 == 0:
            # print("t={0:7d}, span={1:2d}".format(t, span))

def som_test(som):
    """ テストフェーズ """
    result = np.zeros(num_lines)

    for i in range(num_lines):
        for j in range(SOM_IN_UNIT):
            num_ch = j + 1
            ch = "ch" + str(num_ch)

            som.input_data[j] = data[ch][i]

        som_win_unit(som)
        result[i] = som.winner_unit
        return result

def som_win_unit(som):
    """ 勝者ユニットの探索 """
    # 初期化
    for j in range(SOM_IN_UNIT):
        min_dis = pow(som.input_data[j] - som.map_l[0].weight[j], 2)
    som.winner_unit = 0

    # 探索
    for i in range(1, SOM_MAP_UNIT):
        distance = 0.0

        for j in range(SOM_IN_UNIT):
            distance += pow(som.input_data[j] - som.map_l[i].weight[j], 2)

        if distance < min_dis:
            min_dis = distance
            som.winner_unit = i

def set_data():
    pass

if __name__ == "__main__":
    som_main()
