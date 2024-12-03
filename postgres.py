import psycopg2
import time


def connect_to_db():
    """Connect to PostgreSQL database and return the connection object."""
    try:
        connection = psycopg2.connect(
            host="localhost",  # Remplacez par l'adresse de votre serveur
            database="mydatabase",  # Nom de la base de données
            user="myuser",  # Nom d'utilisateur
            password="mypassword"  # Mot de passe
        )
        print("Connexion réussie à la base de données PostgreSQL")
        return connection
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return None


def measure_query_time(connection, query):
    """Execute a query and measure the time it takes to complete."""
    cursor = connection.cursor()
    start_time = time.time()  # Démarrer le chronomètre
    cursor.execute(query)
    end_time = time.time()  # Arrêter le chronomètre

    execution_time = end_time - start_time
    print(f"Requête exécutée en {execution_time:.6f} secondes")

    # Récupérer les résultats si c'est une requête SELECT
    if query.strip().lower().startswith("select"):
        results = cursor.fetchall()
        print(f"Nombre de résultats : {len(results)}")

    cursor.close()
    return execution_time

#Sample
def main():
    """Main function to connect and run queries."""
    connection = connect_to_db()

    if connection:
        try:
            queries = [
                "SELECT * FROM my_table LIMIT 100;",
                "SELECT COUNT(*) FROM my_table;",
                "SELECT * FROM my_table WHERE column = 'value';"
            ]

            for query in queries:
                print(f"\nExécution de la requête : {query}")
                measure_query_time(connection, query)
        finally:
            connection.close()
            print("Connexion fermée.")


if __name__ == "__main__":
    main()
