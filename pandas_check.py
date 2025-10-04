import pandas as pd

def main():

    data = pd.read_csv("weather_data.csv")
    print(data)
    print(data['temp'])

if __name__ == '__main__':
    main()

