from pymongo import MongoClient


def get_indian_cuisines(collection):
    return list(
        collection.find({'cuisine': 'Indian'}, {'_id': False, 'name': 1, 'cuisine': 1}))


def get_indian_and_thai_cuisines(collection):
    return list(collection.find(
        {'$or': [{'cuisine': 'Indian'}, {'cuisine': 'Thai'}]}, {'_id': False, 'name': 1, 'cuisine': 1}))


def get_specific_address(collection):
    return list(collection.find(
        {'address.building': "1115", 'address.street': 'Rogers Avenue', 'address.zipcode': '11226'}, {'_id': False, 'name': 1, 'cuisine': 1}))


def ex_1(collection):
    print('*** Ex1 ***')
    ex1_1 = get_indian_cuisines(collection)
    print('\nEx1.1')
    for restaurant in ex1_1:
        print(restaurant)

    ex1_2 = get_indian_and_thai_cuisines(collection)
    print('\nEx1.2')
    for restaurant in ex1_2:
        print(restaurant)

    ex1_3 = get_specific_address(collection)
    print('\nEx1.3')
    for restaurant in ex1_3:
        print(restaurant)


def insert_specific_one(collection):
    collection.insert_one({
        'restaurant_id': '41704620',
        'borough': 'Manhattan',
        'name': 'Vella',
        'cuisine': 'Italian',
        'address': {
            'building': '1480',
            'street': '2 Avenue',
            'zipcode': '10075',
            'coords': [-73.9557413, 40.7720266]
        },
        'grades': [
            {
                'date': '2014-10-11T00:00:00.000+00:00',
                'grade': 'A',
                'score': 11,
            }
        ]
    })

    return collection.find_one({'restaurant_id': '41704620'}, {'_id': False, 'name': 1, 'restaurant_id': 1})


def ex_2(collection):
    print('*** Ex2 ***')
    ex2_1 = insert_specific_one(collection)
    print('\nEx2.1')
    print(ex2_1)


def delete_one_manhattan(collection):
    return collection.delete_one({'borough': 'Manhattan'})


def delete_all_thai_cuisines(collection):
    return collection.delete_many({'cuisine': 'Thai'})


def ex_3(collection):
    print('*** Ex3 ***')
    ex3_1 = delete_one_manhattan(collection)
    print('\nEx3.1')
    print(ex3_1.deleted_count)
    ex3_2 = delete_all_thai_cuisines(collection)
    print('\nEx3.2')
    print(ex3_2.deleted_count)


def get_specific_street(collection):
    return list(collection.find({'address.street': 'Rogers Avenue'}, {'_id': False, 'restaurant_id': 1, 'name': 1, 'address.street': 1}))


def update_restaurants(collection, restaurants):
    deleted = 0
    updated = 0
    for restaurant in restaurants:
        r = collection.find_one(
            {'restaurant_id': restaurant.get('restaurant_id')}, {'grades': 1})
        if r:
            grades = list(filter(lambda x: x.get('grade') ==
                                 'C', list(r.get('grades'))))
            if len(grades) > 1:
                deleted += collection.delete_one(
                    {'restaurant_id': restaurant.get('restaurant_id')}).deleted_count
            else:
                updated += collection.update_one(
                    {'restaurant_id': restaurant.get('restaurant_id')}, {'$push': {'grades': {
                        'date': '2022-04-25T00:00:00.000+00:00',
                        'grade': 'C',
                        'score': 7,
                    }}}).modified_count


def ex_4(collection):
    print('*** Ex4 ***')
    ex4_1 = get_specific_street(collection)
    print('Ex4.1')
    for restaurant in ex4_1:
        print(restaurant)

    ex4_2 = update_restaurants(collection, ex4_1)


client = MongoClient("mongodb://localhost/27017")

db = client['test']

collection = db['restaurants']

ex_1(collection)
ex_2(collection)
ex_3(collection)
ex_4(collection)
