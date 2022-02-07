import json
import pickle

import numpy
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, bed, bath, car):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bed
    x[1] = bath
    x[2] = car
    if loc_index >= 0:
        x[loc_index] = 1

    return round(numpy.float64(__model.predict([x])[0]),2)


def get_location_names():
    global __locations

    return __locations


def load_saved_artefacts():
    print('Loading saved artefacts...')
    global __data_columns
    global __locations

    with open('./artefact/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open('./artefact/sydney_price_pred_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("End of loading")


if __name__ == '__main__':
    load_saved_artefacts()
    print(get_location_names())
    print(get_estimated_price('Avalon Beach', 4, 2, 2))
    print(get_estimated_price('Avalon Beach', 4, 3, 4))
    print(get_estimated_price('Avalon Beach', 3, 1, 2))
    print(get_estimated_price('Avalon Beach', 3, 1, 2))
    print(get_estimated_price('Avalon Beach', 5, 4, 4))

