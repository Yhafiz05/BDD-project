import time
import pymonetdb

def connect_to_monetdb():
    try:
        conn = pymonetdb.connect(
            user="monetdb",
            password="monetdb",
            host="localhost",
            port=50000,
            database="spotify"
        )
        print("Connexion réussie à la base de données Monetdb")
        return conn
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return None

# Fonction pour mesurer le temps d'exécution d'une requête
def measure_query_time(query):
    conn = connect_to_monetdb()
    cursor = conn.cursor()

    start_time = time.time()  # Temps avant l'exécution de la requête

    cursor.execute(query)
    result = cursor.fetchall()  # Récupérer tous les résultats

    end_time = time.time()  # Temps après l'exécution de la requête

    # Calcul du temps d'exécution
    execution_time = end_time - start_time
    print(f"Temps d'exécution de la requête : {execution_time:.6f} secondes")

    cursor.close()
    conn.close()

    return result, execution_time

def main():
    # Exemple de requête
    query = """SELECT * FROM podcast_rankings where region = 'us' limit 10;"""

    # Exécution et mesure du temps de la requête
    result, exec_time = measure_query_time(query)

    # Affichage des résultats
    print("\nRésultats de la requête:")
    for row in result:
        print(row)

    # Affichage du temps total
    print(f"\nTemps d'exécution total de la requête : {exec_time:.6f} secondes")

if __name__=="__main__":
    list = [] #Tableau à utiliser pour recupérer les temps d'exécution
    connect_to_monetdb()
    main()