import json
import psycopg2

file_path = r'C:\Users\Godhane computer\Documents\data_visualization_project\jsondata.json'


with open(file_path, 'r') as f:
    file_content = f.read()
    print("File content read successfully:")
    print(file_content)  

    try:
        data = json.loads(file_content)
        print("JSON data loaded successfully.")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        raise


conn = psycopg2.connect(
    dbname="datavis_db", user="postgres", password="yourpassword", host="localhost"
)
cur = conn.cursor()

for item in data:
    cur.execute("""
        INSERT INTO data (intensity, likelihood, relevance, year, country, topics, region, city, sector, pest, source, swot)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        item['intensity'], item['likelihood'], item['relevance'], item['year'],
        item['country'], item['topics'], item['region'], item['city'],
        item.get('sector'), item.get('pest'), item.get('source'), item.get('swot')
    ))

conn.commit()
cur.close()
conn.close()


