import pandas as pd
import sys
import os

if __name__=="__main__":
    dataPath = sys.argv[1]
    outDir = sys.argv[2]
    snakeDf = pd.read_csv(dataPath)

    snakeDfDict = snakeDf.to_dict('records')
    data = []
    for snake in snakeDfDict:
        if snake['country']=='India':
            snakeImgPath = snake['image_path']
            os.system(f'cp {snakeImgPath} {outDir}')
            record = snake.copy()
            record['image_path'] = outDir + snakeImgPath.split('/')[-1]
            data.append(record)

    df = pd.DataFrame.from_records(data)
    df.to_csv('IndianSnakesMeta.csv')
