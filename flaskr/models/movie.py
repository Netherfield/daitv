from database.connection_manager import *

class Movie:
    """
    ID, Title, Year, Original
    NO GENRE at the moment
    """
    def __init__(self, id, title, year, original=None):
        self.id = id
        self.title = title
        self.year = year
        if original != "":
            self.original = original
        else:
            self.original = None

    @staticmethod
    def get_all_mongodb(collection):
        """
        ritorna * from collection
        :param collection:
        :return:
        """
        db = mongodb_type()
        colx = db[collection]
        results = colx.find()
        obj_list = [Movie(x["MovieID"], x["Title"], x["Year"], x["Original"]) for x in results]
        return obj_list

    @staticmethod
    def get_all_sqlite(TABLE_NAME, DB_PATH=None):
        """
        DB_PATH = "../database/sample/DAITV"
        ritorna * from SQLite Local DB
        :return:
        """
        if DB_PATH == None:
            DB_PATH = "../database/sample/DAITV"
        QUERY = f"SELECT * FROM {TABLE_NAME}"
        conx = sqlite3.connect(DB_PATH)
        cursor = conx.cursor()
        cursor.execute(QUERY)
        data = cursor.fetchall()
        conx.close()
        obj_list = [Movie(x[0], x[1], x[2], x[3]) for x in data]
        return obj_list


    @staticmethod
    def get_one_sqlite(TABLE_NAME, film_id, DB_PATH=None):
        """
        ritorna il film nell'argomento
        :param TABLE_NAME:
        :param DB_PATH:
        :return:
        """
        if DB_PATH == None:
            DB_PATH = "../database/sample/DAITV"
        QUERY = f"SELECT * FROM {TABLE_NAME} where ID = {film_id}"
        conx = sqlite3.connect(DB_PATH)
        cursor = conx.cursor()
        cursor.execute(QUERY)
        data = cursor.fetchall()
        conx.close()
        movie = [Movie(x[0], x[1], x[2], x[3]) for x in data]
        return movie[0]


    def to_dict(self):
        """
        return dict info
        :return:
        """
        return {
            "MovieID": self.id,
            "Title": self.title,
            "Year": self.year,
            "Original": self.original
        }

