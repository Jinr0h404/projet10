import pytest
from User.models import CustomUser


@pytest.mark.django_db
def test_custom_user_model():
    """test that the CustomUser model records the user in the database"""
    username = "test_user"
    email = "troubadour@gmail.com"
    password = "Troubadour"
    user = CustomUser.objects.create_user(
        username=username, email=email, password=password
    )
    expected_value = "test_user | troubadour@gmail.com"
    assert str(user) == expected_value
