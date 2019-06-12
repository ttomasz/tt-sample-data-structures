from text_search import idf_matrix, search
import csv

if __name__ == "__main__":
    data = {}
    # file with data from twitter downloaded from kaggle
    path = r'/home/tomasz/Pobrane/training.1600000.processed.noemoticon.csv'
    with open(path, 'r', encoding='ISO-8859-1') as f:
        tweets = csv.reader(f)
        for idx, row in enumerate(tweets, 1):
            data[row[1]] = row[5].replace('&quot;', '"')
            if idx == 300000: break  # load only 300 000 tweets for this test
    
    baza = idf_matrix(data)
    wynik = search('the weather today', baza)
    for i in range(10):
        print(wynik[i])
        print(data[wynik[i][0]])
