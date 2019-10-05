import pytest


def test_input(tfidf_instance):
    with pytest.raises(ValueError):
        tfidf_instance.get_n_max_common(-1)

        corpus_size = len(tfidf_instance.global_counter)
        tfidf_instance.get_n_max_common(corpus_size+1)