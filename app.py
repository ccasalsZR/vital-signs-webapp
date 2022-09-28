# import secrets
from flask import Flask, render_template
# import snowflake.connector
# import pandas as pd
# import json
import jwt
import time
import os

METABASE_SITE_URL = os.getenv('METABASE_SITE_URL')
METABASE_SECRET_KEY = os.getenv('METABASE_SECRET_KEY')


payload = {
  "resource": {"question": 3},
  "params": {
    
  },
  "exp": round(time.time()) + (60 * 10) # 10 minute expiration
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

# iframeUrl = METABASE_SITE_URL + "/embed/question/" + token.decode('utf-8') + "#bordered=true&titled=false"

# conn = snowflake.connector.connect(
#     user = os.getenv('DB_SNOW_USER'),
#     password= os.getenv('DB_SNOW_PASS'),
#     account='jt36375.eu-central-1',
#     warehouse='X_SMALL_WH',
#     database='DATAHUB'
#     # role='VITAL_SIGNS'
# )

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')


def index():

    # data = [
    #     ('01-01-2022',1597),
    #     ('01-02-2022',1496),
    #     ('01-03-2022',1908),
    #     ('01-04-2022',896),
    #     ('01-05-2022',755),
    #     ('01-06-2022',453),
    #     ('01-07-2022',1100),
    # ]

    # labels = [row[0] for row in data]
    # values = [row[1] for row in data]

    # # execute SQL statement via cursor
    # cur=conn.cursor()
    # cur.execute('''
    #     WITH CASH_FLOW AS (
    #             SELECT SUM(INVESTMENT_CF) + SUM(OPERATING_CF) AS FREE_CASH_FLOW 
    #             FROM ACCESS_LAYER.VS_VIEW_NWC_CASHFLOW  
    #             WHERE 1=1
    #                 AND SUBSEGMENT LIKE 'Group%'
    #                 AND DATE_TRUNC(YEAR,DATEEXTRACT) = DATE_TRUNC(YEAR,CURRENT_DATE())
    #         ) 
    #         ,PERFORMANCE_VIEW AS (
    #             SELECT SUM(IFF(CODE = 'PV300000', VALUE_CHF, 0)) AS EXTERNAL_REVENUE 
    #                 ,SUM(IFF(CODE = 'PV500500', VALUE_CHF, 0)) AS CONTRIBUTION_MARGIN_3
    #             FROM ACCESS_LAYER.VS_VIEW_PERFORMANCE_VIEW_2  
    #             WHERE 1=1
    #                 AND "TYPE" = 'perf_view'
    #             --	AND SEGMENT = 'Group'
    #                 AND DATE_TRUNC(YEAR,DATEEXTRACT) = DATE_TRUNC(YEAR,CURRENT_DATE())
    #         )
    #     SELECT * 
    #     FROM CASH_FLOW
    #     LEFT JOIN PERFORMANCE_VIEW
    # ''')

    # df = pd.DataFrame(cur.fetchall())

    # free_cash_flow = df.iloc[0][0]
    # external_revenue = df.iloc[0][1]/1000
    # contribution_margin_3 = df.iloc[0][2]/1000

    first_name = 'Carlos'
    stuff = 'This is <strong> Bold Text</strong>'

    
    return render_template('index.html',first_name=first_name
        ,stuff=stuff
        ,METABASE_SECRET_KEY=METABASE_SITE_URL
        # ,labels=labels
        # ,values=values
        # ,iframeUrl=iframeUrl
        # ,free_cash_flow=free_cash_flow
        # ,external_revenue=external_revenue
        # ,contribution_margin_3=contribution_margin_3
        )

@app.route('/user/<name>')

def user(name):
    return render_template('user.html', user_name = name)


#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


# if __name__ == '__main__':
#     app.run(debug=True)