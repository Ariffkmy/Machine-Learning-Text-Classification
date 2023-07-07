
# coding: utf-8

# In[5]:

from flask import Flask , request
from flask_restplus import Api , Resource , fields
from flask_cors import CORS, cross_origin
from waitress import serve
#import ChromeExtensionAPI_controller as controller



# In[6]:


import Controller as controller


# In[2]:

flask_app = Flask(__name__)
CORS(flask_app)
app = Api(app = flask_app,
		  version = "1.0",
		  title = "Arif Backend",
		  description = "")

#app.config['CORS_HEADERS'] = 'Content-Type'
name_space = app.namespace('Arifh', description='Manage names')

#cors = CORS(app)
@name_space.route("/inner/",methods =['POST'])
#@cross_origin()
class Inner(Resource):
	#@app.expect(model)
    def post(self):
        try:
            data_req = request.get_json()
            name=data_req['name']
            print(name)
            studentid=data_req['studentid']
            print(name)
            ptitle=data_req['ptitle']
            print(ptitle)
            feedback=data_req['feedback']
            print(feedback)
            email=data_req['email']
            print(email)
            results =  controller.Call_function(name,studentid,email,ptitle,feedback)
            #results = controller.Call_function("Ariff Hakimi ","24480","asd@adsf.com","Idk","THis was a good project")
            return results
        except KeyError as e:
            print(e)
            name_space.abort(500, e.__doc__, status="Could not save information", statusCode="500")
        except Exception as e:
            print(e)
            name_space.abort(400, e.__doc__, status="Could not save information", statusCode="400")

# In[ ]:


if __name__ == "__main__":
    # app.run() ##Replaced with below code to run it using waitress
    serve(flask_app, host='0.0.0.0', port=5000)




