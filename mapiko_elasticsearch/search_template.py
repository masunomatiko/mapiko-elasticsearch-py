import elasticsearch


class SearchTemplate:
    def __init__(self, path_script: str) -> None:
        self.path_script = path_script

    def put(self) -> None:
        with open('tests/_scripts/test_script.json') as f:
            body = f.read()

        es = elasticsearch.Elasticsearch()
        try:
            response = es.put_script(
                id='test_script',
                body=body
            )
        except elasticsearch.ElasticsearchException as e:
            raise e

        if 'acknowledged' in response.keys():
            return
        else:
            raise Exception('UnexpectedResponse')
