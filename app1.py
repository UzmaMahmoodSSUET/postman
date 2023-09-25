from flask import Flask, request, jsonify



app = Flask(__name__)

stores = [
    {
        'name': 'beautiful store',
        'items': [
                    {'name': 'flowers', 'price': 100 }
                  ]
    },
    {
        'name': 'beautiful store 2',
        'items': [
                  {'name': 'books', 'price': 100 }
                 ]
    }
]


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def Welcome():
    return '<h1> Welcome to store</h1>'


@app.route('/store')
def get_all_store_name():
   return jsonify({'stores': stores})


@app.route('/store', methods= ['POST'])
def create_store():
   request_data = request.get_json()
   new_store = {
      'name': request_data['name'],
      'items':[]
   }
   stores.append(new_store)
   return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store_name(name):
   
   for store in stores:
    if(store['name'] == name):
        return jsonify(store)
    return jsonify({'message': 'store not found'})
 


if __name__ == '__main__':
   app.run(debug = True)
