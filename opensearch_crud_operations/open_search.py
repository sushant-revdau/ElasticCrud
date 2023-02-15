from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[
        {"host": "localhost",
         "port": 9200}],
    http_auth=("admin", "admin"),
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)
