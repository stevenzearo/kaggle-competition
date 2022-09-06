import pandas as pd

from common.file.file_reader import read_file

if __name__ == '__main__':
    data: pd.DataFrame = read_file("../../dataset/train.csv", "utf8")
    print(data.columns)
    pass