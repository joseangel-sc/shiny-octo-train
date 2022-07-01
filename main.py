from mysql import connector
from items import ITEMS

CREDENTIALS = {'host': 'db',
               'port': 3306,
               'user': 'pinner',
               'database': 'pinterest', 
               'password': 'pintastic'}



def create_connector():
    return connector.connect(**CREDENTIALS)


def create_items_table(): 
    with create_connector() as conn:
        with conn.cursor() as cursor: 
            cursor.execute('''create table if not exists ITEMS (
                              itemId int, 
                              itemNumber int)
                            ''')
            for _id, item in enumerate(ITEMS):                
                cursor.execute(f"insert into ITEMS (itemId, itemNumber) values ({_id}, {item})")
            conn.commit() 
            

