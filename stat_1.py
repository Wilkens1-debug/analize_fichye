from csvstat.csv import CSVStatsAnalyzer
if __name__ == "__main__":

    filename = input("Antre chemen ou: ")
analyzer = CSVStatsAnalyzer(filename)
stats = analyzer.analyze_csv()
