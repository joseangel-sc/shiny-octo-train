from logic.db_utils import run_query


def create_post(author_id, post_text): 
    query = f"insert into posts (author_id, post_text) values ({author_id}, '{post_text}')"
    run_query(query)


def get_post(post_id, viewer_id): 
    query_get_post = f"select * from posts where post_id = {post_id}"
# TODO    query_update_seen_times = 
    return run_query(query_get_post)





