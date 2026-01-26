import duckdb

con = duckdb.connect()

query = """
WITH daily_max AS (
    SELECT
        DATE(lpep_pickup_datetime) AS pickup_day,
        MAX(trip_distance) AS max_trip_distance
    FROM read_parquet('green_tripdata_2025-11.parquet')
    WHERE trip_distance < 100
    GROUP BY 1
)
SELECT
    pickup_day,
    max_trip_distance
FROM daily_max
ORDER BY max_trip_distance DESC
LIMIT 1
"""

result = con.execute(query).fetchone()

print("Pickup day with longest trip (<100 miles):", result[0])
print("Longest trip distance:", result[1])
