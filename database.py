from datetime import datetime
import psycopg2

class Database:
    """En abstrakt klass för databas-anslutning och -kommandon."""

    def __init__(self):
        """Inititera databas-anslutning."""
        self.connection = psycopg2.connect("host=localhost dbname=daodao1a user=monitoring")
        self.cursor = self.connection.cursor()

    def log_entry(self, measurement: float):
        """Skapa en ny rad i databastabellen cpu_measurements i schemat
        monitoring."""

        # Skapa en timestamp från nuvarande tid.
        timestamp_now = datetime.timestamp(datetime.now())

        # Exekvera INSERT-kommando.
        self.cursor.execute("INSERT INTO monitoring.cpu_measurements (timestamp,measurement) VALUES (%s,%s)", (timestamp_now, measurement))
        self.connection.commit()

    def get_entries(self, limit = None):
        """Returnera rader från databastabellen cpu_measurements i schemat
        monitoring, med valfri
        begränsning av returnerade rader."""

        self.cursor.execute("SELECT * FROM monitoring.cpu_measurements ORDER BY timestamp DESC")
        result = None
        try:
            result = self.cursor.fetchmany(limit)
        except ProgrammingError:
            print("No result")

        return result

