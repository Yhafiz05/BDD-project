import time
import pymonetdb

# Paramètres de connexion
HOST = "localhost"  # Hôte de la base de données
PORT = 50000  # Port par défaut de MonetDB
DATABASE = "your_database"  # Nom de la base de données
USER = "monetdb"  # Utilisateur de connexion
PASSWORD = "your_password"  # Mot de passe de l'utilisateur

# Connexion à la base de données
def connect_to_monetdb():
    conn = pymonetdb.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)
    return conn

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

# Exemple de requête
query = """
SELECT users.username, COUNT(orders.id) AS total_orders
FROM users
JOIN orders ON users.id = orders.user_id
GROUP BY users.username
ORDER BY total_orders DESC
LIMIT 10;
"""

# Exécution et mesure du temps de la requête
result, exec_time = measure_query_time(query)

# Affichage des résultats
print("\nRésultats de la requête:")
for row in result:
    print(row)

# Affichage du temps total
print(f"\nTemps d'exécution total de la requête : {exec_time:.6f} secondes")
