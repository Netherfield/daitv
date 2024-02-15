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

    def to_dict(self):
        """
        return dict info
        :return:
        """
        return {
            "type" : self,
            "MovieID": self.id,
            "Title": self.title,
            "Year": self.year,
            "Original": self.original
        }
