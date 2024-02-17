from database import connection_manager as cm

try:
    conx = cm.sqlite3.connect("DAITV")
    cursor = conx.cursor()
    with open("queries.sql") as f:
        cursor.executescript(f.read())
except Exception as e:
    print(f"errore: {e}")
