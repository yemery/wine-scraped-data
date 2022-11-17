import resource
# from flask import Flask
# from flask_restful import Api,Resource
import json
# app=Flask(__name__)

# api=Api(app)
# if __name__=='__main__':
#     app.run(debug=True)
# class getInfo(Resource):
#     def get(self,gr):
#         return
f=open('data.json')
data=json.load(f)
for i in data['101']:
    print(i)
