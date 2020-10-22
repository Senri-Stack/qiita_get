import json
import requests
import pandas as pd
import time

def QiitaGet():
    #新規記事を10件取得
    url = 'http://qiita.com/api/v2/items'
    params = {'page': '1', 'per_page': '10'}
    new_articles = requests.get(url, params=params).json()
    time.sleep(180)

    # 辞書リストをデータフレーム型に変換。
    df = pd.io.json.json_normalize(new_articles)

    df = df[['title', 'tags', 'url','user.name','user.id']]

    #CSVに書き込み、任意のファイル名で保存
    df.to_csv("QiitaGet.csv")

if __name__ == '__main__':
    QiitaGet()
