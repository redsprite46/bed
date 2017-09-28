import pandas as pd

result_knn = pd.read_csv(
    'C:/Users/ROBO-E-03/Desktop/scope/data/result_KNN.csv', header=None,
    encoding="Shift_JIS")
print(result_knn)
records = []
records.append(result_knn)
result = pd.DataFrame(records)
result.to_csv('C:/Users/ROBO-E-03/Desktop/scope/data/summarize.csv')