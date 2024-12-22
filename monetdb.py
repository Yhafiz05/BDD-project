import csv
import time
import random

import pymonetdb
from datetime import datetime, timedelta
def connect_to_db():
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

def measure_query_time(connection, query):
    """Execute a query and measure the time it takes to complete."""
    cursor = connection.cursor()
    start_time = time.time()  # Start timer
    cursor.execute(query)
    end_time = time.time()  # Stop timer

    execution_time = end_time - start_time
    print(f"Query executed in {execution_time:.6f} seconds")
    cursor.close()
    return execution_time

def insert_data(connection):
    # Exemple de requête d'insertion
    insert_query_template = """
    INSERT INTO podcast_rankings (
        date, rank, region, chart_rank_move, episode_uri, show_uri, episode_name, description, 
        show_name, show_description, show_publisher, duration_ms, explicit, is_externally_hosted, 
        is_playable, language, languages, release_date, release_date_precision, show_copyrights, 
        show_explicit, show_href, show_html_description, show_is_externally_hosted, show_languages, 
        show_media_type, show_total_episodes, show_type, show_uri2
    ) VALUES (
        '{date}', {rank}, 'US', {chart_rank_move}, 'episode_uri_{rank}', 'show_uri_{rank}', 
        'Episode {rank}', 'Description of episode {rank}', 'Show {rank}', 
        'Description of show {rank}', 'Publisher {rank}', {duration_ms}, false, false, 
        true, 'en', 'en,fr', '{release_date}', 'day', 'Copyright {rank}', 
        false, 'https://show_uri_{rank}', '<html>Description of show {rank}</html>', 
        false, 'en,es', 'audio', {total_episodes}, 'podcast', 'show_uri2_{rank}'
    );
    """

    # Boucle pour insérer 500 enregistrements avec des valeurs variables
    data = []
    for i in range(1, 501):  # Insertion de 500 lignes
        date = f"2024-01-{i % 31 + 1:02d}"  # Exemple de date dynamique
        rank = i
        chart_rank_move = random.randint(-50, 50)
        duration_ms = random.randint(1000000, 3000000)  # Durée entre 1M et 3M ms
        release_date = date
        total_episodes = random.randint(1, 500)

        # Génération de la requête d'insertion
        query = insert_query_template.format(
            date=date,
            rank=rank,
            chart_rank_move=chart_rank_move,
            duration_ms=duration_ms,
            release_date=release_date,
            total_episodes=total_episodes
        )

        # Mesurer le temps d'exécution pour chaque insertion
        execution_time = measure_query_time(connection, query)

        # Stocker le résultat avec l'index de la ligne et le temps d'exécution
        data.append([i, execution_time])

    return data

def main():
    """Main function to connect and run queries."""
    connection = connect_to_db()

    if connection:
        try:
            '''
            queries = [
                "SELECT date FROM podcast_rankings WHERE date > '2024-09-01' AND date < '2024-10-01' OFFSET 0;",
            ]

            for query in queries:
                print(f"\nExecuting query: {query}")
                data = []
                for i in range(0, 500):
                    data.append([i, measure_query_time(connection, query)])

                # Write results to a CSV file
                with open("basicOutput.csv", mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(data)

        finally:
            connection.close()
            print("Connection closed.")
        '''

            data = insert_data(connection)

            # Sauvegarder les résultats dans un fichier CSV
            with open("basicOutput.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data)

            print("Données insérées avec succès et résultats enregistrés.")

        finally:
            connection.close()
            print("Connexion fermée.")

if __name__ == "__main__":
    main()