import psycopg2
import psycopg2.extensions


class DataBase:
    def __init__(self):
        self.host = "localhost"
        self.port = 5432
        self.database = "postgres"
        self.user = "postgres"
        self.password = "postgres"
        self.init_connection()
        self.init_cursor()
        self.init_database()

    @property
    def connection(self) -> psycopg2.extensions.connection:
        return self.connection

    @connection.setter
    def connection(self, value):
        self.connection = value

    @property
    def cursor(self) -> psycopg2.extensions.cursor:
        return self.cursor

    @cursor.setter
    def cursor(self, value):
        self.cursor = value

    def init_connection(self):
        self.connection: psycopg2.extensions.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password,
        )

    def init_cursor(self):
        self.cursor: psycopg2.extensions.cursor = self.connection.cursor()

    def init_database(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS high_scores (
                name varchar(50),
                score integer
            );
        """
        self.cursor.execute(create_table_query)

    def save_score(self):
        pass

    def __del__(self):
        self.cursor.close()
        self.connection.close()
