from tests.test_params import generic_tests_params
from tests.conftest import validate_tfidf_res


def test_sanity(tfidf_instance, tfidf_instance_same_paths_twice):
    tfidf_res = tfidf_instance.get_n_max_common(generic_tests_params['max_words'])
    tfidf_res_dup = tfidf_instance_same_paths_twice.get_n_max_common(generic_tests_params['max_words'])
    validate_tfidf_res([tfidf_res, tfidf_res_dup])
