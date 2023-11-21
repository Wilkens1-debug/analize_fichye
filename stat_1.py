from csvstat.csv import  ExcelStatsAnalyzer
if __name__ == "__main__":

    nom_fichier_excel =  input("Entrer votre chemin(path): ")
analyseur_excel = ExcelStatsAnalyzer(nom_fichier_excel)


resultat_excel = analyseur_excel.analyze_excel()


donnees_chaines_excel = resultat_excel["strings"]
donnees_floats_excel = resultat_excel["floats"]
donnees_entiers_excel = resultat_excel["integers"]


print("Données de chaînes de caractères :", donnees_chaines_excel)
print("Données de nombres décimaux :", donnees_floats_excel)
print("Données d'entiers :", donnees_entiers_excel)

print("")