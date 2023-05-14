from psycopg2 import connect
from psycopg2.extensions import connection as ConnectionType
from psycopg2.extensions import cursor as CursorType


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

    def check_table(self, table: str):
        query_to_print = f"SELECT name, score FROM {table};"
        self.cursor.execute(query_to_print)
        return self.cursor.fetchall()

    def count_query(self, table: str, username: str):
        count_query = f"SELECT COUNT(*) FROM {table} WHERE name = '{username}';"

        self.cursor.execute(count_query)
        return self.cursor.fetchone()[0]

    def add_query(self, table: str, username: str, score: int):
        query_to_add = f"INSERT INTO {table} (name, score) VALUES ('{username}', {score});"

        self.cursor.execute(query_to_add)
        print("Done!")
        return self.connection.commit()

    def update_query(self, table: str, user_name: str, score: int):
        query_to_update = f"UPDATE {table} SET score = {score} WHERE name = '{user_name}';"
        self.cursor.execute(query_to_update)
        return self.connection.commit()

    def select_function(self, table: str, user_name: str, score: int):
        if self.count_query(table, user_name) > 0:
            self.update_query(table, user_name, score)
        else:
            self.add_query(table, user_name, score)

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


testDB = DataBase()
# c = testDB.count_query("high_scores", "aaa")
# print(c)
# b = testDB.add_query("high_scores", "aaa", 45000)
# d = testDB.count_query("high_scores", "aaa")
a = testDB.check_table("high_scores")
# print(d)
print(a)
