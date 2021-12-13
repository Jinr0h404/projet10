import pytest
from Product.views import substitute_getter, count_to_dict
from Product.tests.test_models import product_fixture


@pytest.mark.django_db(reset_sequences=True)
def test_substitute_getter(product_fixture):
    """test that the function properly sorts the list of product id in descending order of common categories"""
    id_product = 1
    expected_value = [(3, 3), (2, 1)]
    sut = substitute_getter(id_product)
    assert sut == expected_value


def test_count_to_dict():
    """test that the function indeed creates a dictionary with a set of key id and value counts the number of common categories"""
    product_list = [2, 3, 5, 7, 9, 2, 5, 9, 5, 9, 9]
    expected_value = {2: 2, 3: 1, 5: 3, 7: 1, 9: 4}
    assert count_to_dict(product_list) == expected_value
