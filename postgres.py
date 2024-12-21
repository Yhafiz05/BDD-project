import psycopg2
import time
import csv


def connect_to_db():
    """Connect to PostgreSQL database and return the connection object."""
    try:
        connection = psycopg2.connect(
            host="localhost",  # Replace with your server address
            database="postgres",  # Database name
            user="postgres",  # Username
            password="admin"  # Password
        )
        print("Successfully connected to the PostgreSQL database")
        return connection
    except Exception as e:
        print(f"Connection error: {e}")
        return None


def drop_all_indexes(connection):
    """Drop all indexes on the podcast_rankings table."""
    cursor = connection.cursor()
    try:
        print("Dropping all indexes on the 'podcast_rankings' table...")
        cursor.execute("""
            SELECT indexname
            FROM pg_indexes
            WHERE tablename = 'podcast_rankings';
        """)
        indexes = cursor.fetchall()

        for index in indexes:
            index_name = index[0]
            print(f"Dropping index: {index_name}...")
            cursor.execute(f"DROP INDEX IF EXISTS {index_name};")

        connection.commit()
        print("All indexes dropped successfully.")
    except Exception as e:
        print(f"Error dropping indexes: {e}")
    finally:
        cursor.close()


def create_brin_index(connection):
    """Create a BRIN index on the date column of podcast_rankings."""
    cursor = connection.cursor()
    try:
        print("Creating BRIN index on the 'date' column...")
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS podcast_rankings_date_brin_idx ON podcast_rankings USING brin (date);")
        connection.commit()
        print("BRIN index created successfully.")
    except Exception as e:
        print(f"Error creating BRIN index: {e}")
    finally:
        cursor.close()


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

def create_btree_index(connection):
    """Create a B-tree index on the date column of podcast_rankings."""
    cursor = connection.cursor()
    try:
        print("Création de l'index B-tree sur la colonne 'date'...")
        cursor.execute("CREATE INDEX IF NOT EXISTS podcast_rankings_date_idx ON podcast_rankings USING btree (date);")
        connection.commit()
        print("Index créé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la création de l'index : {e}")
    finally:
        cursor.close()


def main():
    """Main function to connect and run queries."""
    connection = connect_to_db()

    if connection:
        try:
            # Drop all existing indexes
            drop_all_indexes(connection)

            # Create a BTREE index
#            create_btree_index(connection)

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


if __name__ == "__main__":
    main()
