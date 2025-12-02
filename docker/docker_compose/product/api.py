# Import du framework Flask
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'product': ['iPad Pro 14', 'MacBook Pro', 'Remarkable Pro', 'Ordinateur de bureau']
        }

# Définition d'une route
api.add_resource(Product, '/')

# Exécution de l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
