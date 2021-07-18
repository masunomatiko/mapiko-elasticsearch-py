import pytest
from elasticsearch import ElasticsearchException
from mapiko_elasticsearch import search_template as st


class TestSearchTemplate:
    path_script = 'tests/_scripts/test_script.json'
    response_true = {'acknowledged': True}

    def test_put(self, mocker) -> None:
        mocker.patch(
            'elasticsearch.client.Elasticsearch.put_script',
            return_value=TestSearchTemplate.response_true
        )
        template = st.SearchTemplate(TestSearchTemplate.path_script)
        template.put()

    def test_put_with_exception(self, mocker) -> None:
        template = st.SearchTemplate(TestSearchTemplate.path_script)
        with pytest.raises(ElasticsearchException):
            template.put()
