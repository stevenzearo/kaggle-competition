import pandas as pd
def read_file(file_name: str, encoding: str):
    return pd.read_csv(filepath_or_buffer=file_name, encoding=encoding)

if __name__ == '__main__':
    pass