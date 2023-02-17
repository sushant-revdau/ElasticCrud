from opensearch_crud_operations.open_search import client
from datetime import datetime,timezone

def convert_date():
    date_convert =  datetime.now(timezone.utc).isoformat().replace("+00:00",'')
    converted_date = str(date_convert).split('.')[0]
    return converted_date

async def delete_index(index_name):
    index_exists = client.indices.exists(index=index_name)
    if index_exists:
        client.indices.delete(index=index_name)
        return {'status': True, 'msg': f'Index - {index_name} deleted successfully'}
    return {'status': False, 'msg': f'Index - {index_name} already deleted or does not exists'}


async def update_by_id(index_name, id, doc):
    index_exists = client.indices.exists(index=index_name)
    if index_exists:
        try:
            doc.update({'updated_at':convert_date()})
            return client.update(index=index_name, id=id, body={"doc": doc})
        except ModuleNotFoundError:
            return {'status': False, 'msg': f'id = {id} does not exists'}
    else:
        return {'status': False, 'msg': f'Index = {index_name} does not exists'}


async def delete(index_name, id):
    index_exists = client.indices.exists(index=index_name)
    if index_exists:
        client.delete(index=index_name, id=id)
        return {'status': True, 'msg': f'Index = {index_name} bearing _id = {id} deleted successfully'}
    return {'status': False, 'msg': f'Index - {index_name} already deleted or does not exists'}


async def get_by_id(index_name, id):
    index_exists = client.indices.exists(index=index_name)
    if index_exists:
        try:
            response = client.get(index=index_name, id=id)
            return response['_source']
        except ModuleNotFoundError:
            return {'status': False, 'msg': f'id = {id} does not exists'}
    else:
        return {'status': False, 'msg': f'Index = {index_name} does not exists'}


async def get_by_query(index_name, query):
    result = client.search(index=index_name, body=query)
    result = result['hits']['hits']
    final_list = []
    for res in result:
        final_list.append(res['_source'])
    return final_list


async def get_all(index_name):
    result = client.search(index=index_name, body={"query": {"match_all": {}}})
    result = result['hits']['hits']
    final_list = []
    for res in result:
        final_list.append(res['_source'])
    return final_list


async def create(index_name, mapping):
    index_exists = client.indices.exists(index=index_name)
    if not index_exists:
        client.indices.create(index=index_name)
    mapping.update({'created_at':convert_date(),'updated_at':convert_date()})
    response = client.index(index=index_name, body=mapping)
    response_get_by_id = await get_by_id(index_name=index_name, id=response['_id'])
    try:
        response_get_by_id.update({'id': response['_id']})
        response_update = await update_by_id(index_name=index_name, id=response['_id'], doc=response_get_by_id)
        return await get_by_id(index_name=index_name, id=response_update['_id'])
    except Exception as e:
        return e
