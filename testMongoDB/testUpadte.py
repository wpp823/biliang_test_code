import pymongo
from pymongo import collection
from pymongo.collection import Collection

my_client = pymongo.MongoClient("")
mydb = my_client['mytest']
ssl = mydb['test']
print(ssl)

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

# re = ssl.insert(student)
# print(re)


student = {
    'id': 'ddd',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student_2 = {
    'id': 'www',
    'name': 'Jordan',
    'age': 15,
    'gender': 'male'
}
# re_w = ssl.insert_many([student,student_2])
result = Collection.find_one({'name': 'Mike'})
# print(re_w)

print(type(result))
print(result)
