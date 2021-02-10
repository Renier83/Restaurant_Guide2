import json
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import sqlalchemy
from flask import Flask, request, render_template, jsonify
import os

# Heroku check
is_heroku = False
if 'IS_HEROKU' in os.environ:
    is_heroku = True

# Flask

# SQL Alchemy

# PyMySQL

# Pandas

# JSON

# Import your config file(s) and variable(s)
if is_heroku == True:
    # if IS_HEROKU is found in the environment variables, then use the rest
    # NOTE: you still need to set up the IS_HEROKU environment variable on Heroku (it is not there by default)
    remote_db_endpoint = os.environ.get('remote_db_endpoint')
    remote_db_port = os.environ.get('remote_db_port')
    remote_db_name = os.environ.get('remote_db_name')
    remote_db_user = os.environ.get('remote_db_user')
    remote_db_pwd = os.environ.get('remote_db_pwd')
else:
    # use the config.py file if IS_HEROKU is not detected
    from config import remote_db_endpoint, remote_db_port, remote_db_name, remote_db_user, remote_db_pwd

# Configure MySQL connection and connect
pymysql.install_as_MySQLdb()
engine = create_engine(
    f"mysql://{remote_db_user}:{remote_db_pwd}@{remote_db_endpoint}:{remote_db_port}/{remote_db_name}")

conn = engine.connect()

cityname = "San Juan"
keyword = "all"
price = 0
rating = 0

# Initialize Flask application
app = Flask(__name__)

# Set up your default route


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/city/<cityName>")
def city(cityName=None):
    print("/city/<name>", cityName)

    if cityName == "San Juan":
        fileName = "SanJuan"
    else:
        fileName = cityName

    sql_statement = "SELECT keyword as Type, count(*) as Total from pr.restaurants_tbl where city='" + \
        cityName + "' group by keyword"

    type_df = pd.read_sql(sql_statement, con=engine)

    csvfile = "static/data/" + fileName + ".csv"
    type_df.to_csv(csvfile, index=False)

    sql_statement = "SELECT name as 'Restaurant Name', keyword as Type, business_status as Status, price_level " + \
        "as Price, rating as Rating, address as Address from pr.restaurants_tbl where city = '" + \
        cityName + "' order by keyword, name"

    info_df = pd.read_sql(sql_statement, con=engine)
    print(sql_statement)

    html = info_df.to_html(index=False, table_id='city_tbl', classes='display')

    return render_template('city.html', rating_table=html, cityname=cityName, chart='bar')


@app.route('/search', methods=['POST'])
def search():
    print(f"search")

    cityName = request.form['cityID']
    keyword = request.form['typeID']
    price = request.form['priceID']
    rating = request.form['ratingID']
    chart = request.form['chart']

    print(f"city= {cityName}  {keyword}  {price}  {rating}")

    if cityName == "San Juan":
        fileName = "SanJuan"
    else:
        fileName = cityName

    sql_statement = "SELECT keyword as Type, count(*) as Total from pr.restaurants_tbl where city='" + \
        cityName + "' group by keyword"

    type_df = pd.read_sql(sql_statement, con=engine)

    csvfile = "static/data/" + fileName + ".csv"
    type_df.to_csv(csvfile, index=False)

    sql_statement = "SELECT name as 'Restaurant Name', keyword as Type, business_status as Status, price_level " + \
        "as Price, rating as Rating, address as Address from pr.restaurants_tbl where city='" + cityName + "' "

    if keyword != "all":
        sql_statement = sql_statement + " and keyword='" + keyword + "' "

    if int(price) > 0:
        sql_statement = sql_statement + \
            " and price_level >=" + price + " "

    if int(rating) > 0:
        sql_statement = sql_statement + " and rating >=" + rating + " "

    sql_statement = sql_statement + "order by keyword, rating, price desc"
    print(sql_statement)

    info_df = pd.read_sql(sql_statement, con=engine)
    print(sql_statement)

    html = info_df.to_html(index=False, table_id='city_tbl', classes='display')

    return render_template('city.html', rating_table=html, cityname=cityName, chart=chart)


@app.route('/information')
def information():
    print("/information")

    return render_template('info.html', cityname=cityname)


@app.route('/info', methods=['POST', 'GET'])
def info():
    print("/info")

    cityname = request.form['cityID']

    return render_template('info.html', cityname=cityname)


@app.route('/team')
def team():

    return render_template('team.html')


# set up the data route
@app.route('/api/restaurants')
def get_restaurants():

    # Establish DB connection
    conn = engine.connect()

    query = '''
        SELECT
            *
        FROM
            restaurants
        '''

    resturants_data = pd.read_sql(query, con=conn)
    resturants_json = resturants_data.to_json(orient='records')

    conn.close()
    return resturants_json


if __name__ == "__main__":
    app.run(debug=True)
