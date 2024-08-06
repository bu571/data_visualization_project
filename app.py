from flask import Flask, request, jsonify, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="datavis_db", user="postgres", password="yourpassword", host="localhost"
    )
    return conn

@app.route('/')
def home():
    return "Welcome to the Data Visualization Dashboard"

@app.route('/data', methods=['GET'])
def get_data():
    try:
        filters = {
            "end_year": request.args.get('end_year'),
            "topics": request.args.get('topics'),
            "sector": request.args.get('sector'),
            "region": request.args.get('region'),
            "pest": request.args.get('pest'),
            "source": request.args.get('source'),
            "swot": request.args.get('swot'),
            "country": request.args.get('country'),
            "city": request.args.get('city')
        }
        query = "SELECT * FROM data WHERE TRUE"
        params = []

        for key, value in filters.items():
            if value:
                query += f" AND {key} = %s"
                params.append(value)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        column_names = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()

        result = [dict(zip(column_names, row)) for row in rows]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
@app.route('/dashboard')
def dashboard():
    print("Dashboard route accessed")
    return render_template('dashboard.html')

@app.route('/test')
def test():
    print("Test route accessed")
    return "Test route is working!"

if __name__ == '__main__':
    app.run(debug=True, port=5001)






