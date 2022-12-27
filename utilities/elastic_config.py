from elasticsearch import Elasticsearch
import warnings
warnings.filterwarnings("ignore")

host = 'localhost'
port = 9200
url = f'https://{host}:{port}'
username = 'elastic'
password = 'elastic'
es = Elasticsearch([url],
                   http_auth=(username, password),
                   verify_certs=False
                   )



