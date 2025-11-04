import sqlite3

# Connect to (or create) the SQLite database inside the database folder
conn = sqlite3.connect("buses.db")
cursor = conn.cursor()

# Create the buses table
cursor.execute('''
CREATE TABLE IF NOT EXISTS buses (
    bus_id TEXT PRIMARY KEY,
    route_no TEXT,
    driver_name TEXT,
    capacity INTEGER,
    current_stop TEXT,
    next_stop TEXT,
    status TEXT,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Insert some example data
cursor.executemany('''
INSERT OR REPLACE INTO buses (bus_id, route_no, driver_name, capacity, current_stop, next_stop, status)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    ('BUS001', '101', 'Ravi Kumar', 45, 'Main Station', 'City Center', 'On Time'),
    ('BUS002', '102', 'Anil Singh', 40, 'Old Town', 'University', 'Delayed'),
    ('BUS003', '101', 'Vikram Rao', 50, 'City Center', 'Tech Park', 'On Time')
])

# Save and close
conn.commit()
conn.close()

print("✅ buses.db created successfully inside database/ folder!")
