from database.connection_manager import *

class User:
    """
    UserID, Gender, Age, Cap, Work, Fascia_eta
    """
    def __init__(self, userID, gender, age, cap, work, fascia_eta):
        self.id = userID
        self.gender = gender
        self.age = age
        self.cap = cap
        self.work = work
        self.fascia_eta = fascia_eta

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
        obj_list = [User(x["UserID"], x["Gender"], x["Age"], x["CAP"], x["Work"], x["fasciaeta"]) for x in results]
        return obj_list

    def to_dict(self):
        """
        return dict info
        :return:
        """
        return {
            "type" : self,
            "UserID": self.id,
            "Gender": self.gender,
            "Age": self.age,
            "CAP": self.cap,
            "Work": self.work,
            "Fascia_eta": self.fascia_eta
        }

