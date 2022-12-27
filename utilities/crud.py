from utilities.elastic_config import *
from uuid import uuid4


def create(index_name, mapping, doc_type):
    index_exists = es.indices.exists(index=index_name)
    if not index_exists:
        es.indices.create(index=index_name)
    response = es.index(index=index_name, body=mapping,
                        doc_type=doc_type, id=uuid4())
    return response


def delete_index(index_name):
    index_exists = es.indices.exists(index=index_name)
    if index_exists:
        es.indices.delete(index=index_name)
        return {'status': True, 'msg': f'Index - {index_name} deleted successfully'}
    return {'status': False, 'msg': f'Index - {index_name} already deleted or does not exists'}


def update(index_name, id, doc):
    response = es.update(index=index_name, id=id, body=doc)
    return response


def delete(index_name, id):
    index_exists = es.indices.exists(index=index_name)
    if index_exists:
        es.delete(index=index_name, id=id)
        return {'status': True, 'msg': f'Index = {index_name} bearing _id = {id} deleted successfully'}
    return {'status': False, 'msg': f'Index - {index_name} already deleted or does not exists'}

# elastic.indices.create(index='some-new-index')

def get(query):
    es.get