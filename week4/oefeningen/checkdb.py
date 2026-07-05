import sqlite3
from datetime import timezone

db = sqlite3.connect("sessions.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
for row in db.execute("SELECT * FROM betalingen"):
    utc_time = row[0].replace(tzinfo=timezone.utc)
    local_time = utc_time.astimezone()

    print(f"{utc_time} \t {local_time} \t {row[1]} \t {row[2]}")

db.close()
