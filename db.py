from psycopg2 import connect
from psycopg2.extensions import connection as ConnectionType
from psycopg2.extensions import cursor as CursorType


class DataBase:
    def __init__(self):
        self.host = "192.168.1.106"
        self.port = 5432
        self.database = "postgres"
        self.user = "postgres"
        self.password = "postgres"
        self.init_connection()
        self.init_cursor()
        self.init_database()

    @property
    def connection(self) -> ConnectionType:
        return self.__connection

    @connection.setter
    def connection(self, value: ConnectionType):
        self.__connection = value

    @property
    def cursor(self) -> CursorType:
        return self.__cursor

    @cursor.setter
    def cursor(self, value: CursorType):
        self.__cursor = value

    def init_connection(self):
        self.connection: ConnectionType = connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password,
        )

    def init_cursor(self):
        self.cursor: CursorType = self.connection.cursor()

    def init_database(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS high_scores (
                name varchar(50),
                score integer
            );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def save_score(self):
        pass

    def count_query(self, table: str, username: str):
        count_query = f"""
        SELECT COUNT(*) FROM {table} WHERE name = '{username}';
        """

        self.cursor.execute(count_query)
        return self.cursor.fetchone()[0]

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


testDB = DataBase()
a = testDB.count_query("high_scores", "aaa")
