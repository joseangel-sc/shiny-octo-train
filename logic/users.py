from logic.db_utils import run_query

DEFAULT_PROFILE_PIC = 'https://www.deviantart.com/e1venbeauty/art/Winnie-The-Pooh-PNG-832237197'


def create_user(username, password, email, user_type, profile_pic=DEFAULT_PROFILE_PIC): 
    query = f"""insert into user 
                (username, user_password, email, user_type, profile_pic) 
                values ('{username}', '{password}', '{email}', '{user_type}', '{profile_pic}')"""
    run_query(query)


def delete_user(user_id_to_delete, user_id_deleting): 
    if is_user_admin(user_id_deleting):
        query = f"""delete from user where user_id = {user_id_to_delete} and user_id != {user_id_deleting}"""
        run_query(query)


def is_user_admin(user_id): 
    query = f"select user_type from user where user_id = {user_id}"
    return 'admin' == run_query(query)[0][0]