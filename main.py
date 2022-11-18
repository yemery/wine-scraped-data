from flask import Flask
from flask_restful import Api,Resource
from scraper import *
# print(myfun)
app=Flask(__name__)
api=Api(app)

@app.route('/')
def getdata():
    myfun=csv_into_json()
    return json.dumps(myfun,indent=4)



if __name__=='__main__':
    app.run(debug=True)
