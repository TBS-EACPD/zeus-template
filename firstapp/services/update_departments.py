from django.utils.functional import cached_property

from firstapp.models import Department


class MissingDepartmentException(Exception):
    def __init__(self, message, missing_ids):
        self.missing_ids = missing_ids
        super().__init__(message)


class UpdateDepartmentsService:
    def __init__(self, json_records, break_if_data_is_missing=True):
        self.json_records = json_records
        self.break_if_data_is_missing = break_if_data_is_missing

    def perform(self):
        return self._update()

    @cached_property
    def ids_in_db(self):
        return set(Department.objects.values_list("id", flat=True))

    def _create_new_departments(self):
        new_records = [r for r in self.json_records if r.id not in self.ids_in_db]
        instances = [Department(**r) for r in new_records]
        return Department.objects.bulk_create(instances)

    def _update(self):
        ids_in_data = {r["id"] for r in self.json_records}
        ids_in_db = set(Department.objects.values_list("id", flat=True))
        if not self.ids_in_db.issubset(ids_in_data):
            self._create_new_departments()

        if self.break_if_data_is_missing and not ids_in_db.issubset(ids_in_data):
            ids_missing_from_data = ids_in_db - ids_in_data
            raise MissingDepartmentException(
                f"The following ids were in this DB, but not in the JSON data: {ids_missing_from_data}",
                missing_ids=ids_missing_from_data,
            )

        depts_to_update = [*Department.objects.filter(id__in=ids_in_data)]
        json_records_by_id = {r["id"]: r for r in self.json_records}

        for d in depts_to_update:
            json_record = json_records_by_id[d.id]
            for attr, val in json_record.items():
                setattr(d, attr, val)

        return Department.objects.bulk_update(
            depts_to_update, fields=self.fields_to_update
        )

    @property
    def fields_to_update(self):
        return [
            "tbs_dept_code",
            "legal_name_en",
            "legal_name_fr",
            "applied_title_en",
            "applied_title_fr",
            "abbr_en",
            "abbr_fr",
        ]


def update_departments(json_records, break_if_data_is_missing=True):
    return UpdateDepartmentsService(
        json_records, break_if_data_is_missing=break_if_data_is_missing
    ).perform()
