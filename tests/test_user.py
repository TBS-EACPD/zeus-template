from firstapp.models import Department


def test_fixture_created_mits_user(client):
    dept = Department.objects.get(tbs_dept_code="MITS")
    user = dept.profile.user
    assert user.check_password("123")
    assert user.is_active
    client.force_login(user)
