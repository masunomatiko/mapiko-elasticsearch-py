import elasticsearch


class SearchTemplate:
    def __init__(self, path_script: str) -> None:
        self.path_script = path_script

    def put(self) -> None:
        es = elasticsearch.Elasticsearch()
        try:
            response = es.client.put_script()
        except elasticsearch.ElasticsearchException as e:
            raise e

        if 'acknowledged' in response.keys():
            return
        else:
            raise Exception('UnexpectedResponse')
