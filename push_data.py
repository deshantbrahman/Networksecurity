import os
import sys

from dotenv import load_dotenv
load_dotenv()

import pandas as pd
import pymongo

from networksecurity.exception.exception import NetworkSecurityException


MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class NetworkDataExtract:

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)

            data.reset_index(drop=True, inplace=True)

            records = data.to_dict(orient="records")

            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            db = mongo_client[database]

            collection = db[collection]

            collection.insert_many(records)

            return len(records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "DESHANTAI"
    COLLECTION = "NetworkData"

    networkobj = NetworkDataExtract()

    records = networkobj.csv_to_json_convertor(
        file_path=FILE_PATH
    )

    print("Number of records:", len(records))

    no_of_records = networkobj.insert_data_mongodb(
        records,
        DATABASE,
        COLLECTION
    )

    print("Inserted records:", no_of_records)