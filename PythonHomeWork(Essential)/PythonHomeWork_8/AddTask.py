import json
import pickle

products = [
    {
        'name': 'Airpods',
        'price': 1500
    },
    {
        'name': 'Iphone 6s',
        'price': 3200
    },
    {
        'name': 'FootWorks',
        'price': 20
    }
]

with open('data/products_pickle.pkl', 'wb') as pickle_file:
    pickle.dump(products, pickle_file)

with open('data/products_pickle.pkl', 'rb') as data_from_pkl:
    prdct = pickle.load(data_from_pkl)

with open('data/products_for_ui.json', 'w') as data_ui:
    json.dump(prdct, data_ui, indent=2)