from django.urls import reverse

from firstapp.models import Report


def test_fixture_created_mits_user(mits, mits_user, mits_client):
    r = Report.objects.create(department=mits, title="title1", body="body1")
    assert r.versions.count() == 1
    assert r.versions.last().edited_by is None

    update_url = reverse("firstapp:update-report", args=[r.pk])
    resp = mits_client.post(update_url, data={"title": "title2", "body": "body2"})
    assert r.versions.count() == 2
    assert r.versions.last().edited_by == mits_user
    assert r.versions.last().body == "body2"
    assert r.versions.last().title == "title2"

