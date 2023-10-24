import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(
        username="testuser",
        first_name="Test",
        last_name="User",
        email="test@example.com",
    )
    assert user.username == "testuser"
    assert user.first_name == "Test"
    assert user.last_name == "User"
    assert user.email == "test@example.com"
    assert user.is_staff is False
    assert user.is_superuser is False
