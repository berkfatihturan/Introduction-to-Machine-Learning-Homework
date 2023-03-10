import pandas as pd

def main():
    dictionary = {"name": ["ali", "veli", "zübeyde", "ahmet", "kubra", "can"],
                  "age": [12, 34, 56, 78, None, 12],
                  "note": [123, 456, 78, 87654, None, 89]}

    dataframe1 = pd.DataFrame(dictionary)
    print(dataframe1)

    print("/****************************/")
    head = dataframe1.head()
    print(head)

    print("/****************************/")
    tail = dataframe1.tail()
    print(tail)

    print("/****************************/")
    print(dataframe1.columns)  # sutunlarin isimlerini verir

    print("/****************************/")
    print(dataframe1.info())  # dataframe hakkında bilgi verir

    print("/****************************/")
    print(dataframe1.dtypes) # dataframe'in her bir column'ın type'ını verir

    print("/****************************/")
    print(dataframe1.describe())

    print("/****************************/")
    print(dataframe1["name"])
    print(dataframe1.loc[:, "age"])  # sadece isimleri getirir
    dataframe1["yeni_future"] = [1, 2, 3, 4, 5, 6]
    print(dataframe1.loc[:3, "age"])
    print(dataframe1.loc[:3, "name":"note"])  # name den note'a kadar olan kolonların ilk 3 satırını yazdırır
    print(dataframe1.loc[::-1])

    filtre1 = dataframe1.age > 10  # yaşı 10'dan büyük olanlar filtrelendi
    dataframe1["bool"] = filtre1
    print(dataframe1.loc[:, ["age", "bool"]])

    filtre2 = dataframe1.note > 100
    filtrelenmis_data2 = dataframe1[filtre2 & filtre1]  # iki filtre birden uyguladık
    print(filtrelenmis_data2)

    dataframe1.dropna(inplace=True)  # dropna ile NaN değerleri sildik
    print(dataframe1)

    dataframe1["yeni2_future"] = [1, 1, 1, 1, 1]
    dataframe1.columns = [each.split('_')[0] + " " + each.split('_')[1] if len(each.split('_')) > 1 else each for each
                          in dataframe1.columns]
    print(dataframe1)


def read_csv_file():
    # Read the CSV file into a DataFrame
    try :
        df = pd.read_csv("C:/Users/{user_name}/Desktop/data.csv")
    except FileNotFoundError:
        pass
    else:
        print(df)


main()