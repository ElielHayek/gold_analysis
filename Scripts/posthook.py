from data_handler import read_sheet_as_dataframe
import lookups
import data_handler  
import database_handler

def truncate_tables():
    db_session = database_handler.create_connection('config.json')
   
    database_handler.close_connection()

