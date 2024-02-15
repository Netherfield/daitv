




from app.objects import Query



def format():
    """decorator to format query output"""
    ...


def create_query(default=True):
    if default:
        from app.web.defaults import DB_CONFIG
        