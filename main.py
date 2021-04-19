from data import Data
from analysis import Analysis 


def main():
    d = Data('./data/weatherAUS.csv')
    a = Analysis(d)
    
    d.preprocess()

if __name__ == "__main__":
    main()
