from flask import Flask, request, jsonify



app = Flask(__name__)

nums=[10,20,30]


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return '<h1> Hello World</h1>'


@app.route("/evenodd<int:num>")
def evenodd(num):
    status= None
    if num%2==0:
        status = "Even"
    else:

        status = "Odd"

    return jsonify({'status':status})
    

@app.route("/addnum", methods=['POST'])
def addnum():
    request_data = request.get_json()
    print(request_data['num'])
    nums.append(request_data['num'])

@app.route("/showlist")
def show():
    return jsonify ({'list':nums})




 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
