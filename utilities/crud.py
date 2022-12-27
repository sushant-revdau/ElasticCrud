from utilities.elastic_config import *
from elasticsearch import helpers
from uuid import uuid4
def create(index_name,mapping):
    index_exists = es.indices.exists(index = index_name)
    if not index_exists:
        es.indices.create(index = index_name)
    response = es.index(index=index_name,body=mapping,id=uuid4())
    return response

def bulk_create(index_name,mapping):
    index_exists = es.indices.exists(index = index_name)
    if not index_exists:
        es.indices.create(index = index_name)
    response = helpers.bulk(es,index=index_name,body=mapping)
    return response

def delete(index_name):
    index_exists = es.indices.exists(index = index_name)
    if index_exists:
        es.indices.delete(index=index_name)
        return {'status':True,'msg':f'Index - {index_name} deleted successfully'}
    return {'status':False,'msg':f'Index - {index_name} already deleted or does not exists'} 

def get_all(index_name):
    response = es.search(index=index_name, query={"match_all": {}})
    return response['hits']

def get_via_id(index_name):
    pass


def delete(index_name, id):
    index_exists = es.indices.exists(index=index_name)
    if index_exists:
        es.delete(index=index_name, id=id)
        return {'status': True, 'msg': f'Index = {index_name} bearing _id = {id} deleted successfully'}
    return {'status': False, 'msg': f'Index - {index_name} already deleted or does not exists'}

# elastic.indices.create(index='some-new-index')

def get(query):
    es.get
