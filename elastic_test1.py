from utilities.crud import create
from utilities.elastic_config import *
from utilities.query_builder import buildElsQuery


# query = buildElsQuery({'name.keyword':'1'})
# print(query)

employees_data = [

    {
        'name': 'Saurav',
        'age': 28,
        'programming_languages': ['Node.js', 'React']
    }
]
emp = [
    {
        "id": 1,
        "name": "Huntlee Dargavel",
        "email": "hdargavel0@japanpost.jp",
        "gender": "male",
        "ip_address": "58.11.89.193",
        "date_of_birth": "11/09/1990",
        "company": "Talane",
        "position": "Research Associate",
        "experience": 7,
        "country": "China",
        "phrase": "Multi-channelled coherent leverage",
        "salary": 180025
    },
    {
        "id": 2,
        "name": "Othilia Cathel",
        "email": "ocathel1@senate.gov",
        "gender": "female",
        "ip_address": "3.164.153.228",
        "date_of_birth": "22/07/1987",
        "company": "Edgepulse",
        "position": "Structural Engineer",
        "experience": 11,
        "country": "China",
        "phrase": "Grass-roots heuristic help-desk",
        "salary": 193530
    },
    {
        "id": 3,
        "name": "Winston Waren",
        "email": "wwaren2@4shared.com",
        "gender": "male",
        "ip_address": "202.37.210.94",
        "date_of_birth": "10/11/1985",
        "company": "Yozio",
        "position": "Human Resources Manager",
        "experience": 12,
        "country": "China",
        "phrase": "Versatile object-oriented emulation",
        "salary": 50616
    },
    {
        "id": 4,
        "name": "Alan Thomas",
        "email": "athomas2@example.com",
        "gender": "male",
        "ip_address": "200.47.210.95",
        "date_of_birth": "11/12/1985",
        "company": "Yamaha",
        "position": "Resources Manager",
        "experience": 12,
        "country": "China",
        "phrase": "Emulation of roots heuristic coherent systems",
        "salary": 300000
    }]
# for data in employees_data:
#     res = es.index(index='employees', document=data)
#     result = query_string(res['_id'])
#     match = es.search(index="employees", body=result
#                       )
#     print(match)

# for em in emp:

#     em.update({'c': date_conversion.convert_date(), 'u': date_conversion.convert_date()})
#     res = es.index(index='employee', document=em)
#     print(res)


employees_data = {
    'name': 'Saurav',
    'age': 28,
    'programming_languages': ['Node.js', 'React']
}


res = create('employee','employee_data',employees_data)
print(res)
