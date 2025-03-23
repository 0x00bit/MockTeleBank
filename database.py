from pymongo import MongoClient


class Database:
    def __init__(self, dbname, collectionname):
        self.client = MongoClient('127.0.0.1', 27017)
        self.dbname = self.client[dbname]
        self.collection = self.dbname[collectionname]

    def createClient(self, username, name, balance=0):
        """Create a new client in the database"""
        try:
            # Preparating the data to add to the database
            client_data = {
                'userid': username,
                'name': name,
                'balance': balance,
                'last_deposit': 0,
                'last_withdraw': 0,
                'transaction_historic': []
            }

            result = self.collection.insert_one(client_data)
            return result.inserted_id
        
        except Exception as err:
            print(f"An error occurred: {err}")

    def getClient(self, userid):
        """Getting information of a client"""
        try:
            client_data = self.collection.find_one({'userid': userid})
            return client_data
        except Exception as err:
            print(f"An error occurred: {err}")

    def updateClient(self, userid, updatedata):
        """Method to update the client information"""
        try:
            result = self.collection.update_one(
                {'userid': userid},
                {'$set': updatedata}
            )
            return result.modified_count
        
        except Exception as err:
            print(f"An error occurred: {err}")
            return None
        
    def deteleClient(self, userid):
        """Method to delete an client from the bank"""
        try:
            result = self.collection.delete_one(
                {'userid':userid}
            )
            return result
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

