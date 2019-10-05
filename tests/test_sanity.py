from . test_params import generic_tests_params


def test_sanity(tfidf_instance):
    tfidf_res = tfidf_instance.get_n_max_common(generic_tests_params['max_words'])
    assert len(tfidf_res) == generic_tests_params['max_words']