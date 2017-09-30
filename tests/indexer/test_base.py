from genekey import indexer


def test_one_feed():
    text = 'abc abq'
    index = indexer.BaseIndexer()
    index.feed(text)

    assert index.get_index() == {'ab': 2, 'bc': 1, 'c ': 1, ' a': 1, 'bq': 1}


def test_empty_feed():
    text = ''
    index = indexer.BaseIndexer()
    index.feed(text)

    assert index.get_index() == {}


def test_no_feed():
    index = indexer.BaseIndexer()

    assert index.get_index() == {}


def test_multiple_feed():
    text1 = 'abc abq'
    text2 = 'bc'
    index = indexer.BaseIndexer()
    index.feed(text1)
    index.feed(text2)

    assert index.get_index() == {
        'ab': 2, 'bc': 2, 'c ': 1, ' a': 1, 'bq': 1, 'qb': 1}
