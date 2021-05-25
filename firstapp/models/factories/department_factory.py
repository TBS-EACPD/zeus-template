import factory

from firstapp.models import Department


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department

    id = factory.Sequence(lambda n: n)
    legal_name_en = factory.Sequence(lambda n: f"The department {n}")
    legal_name_fr = factory.Sequence(lambda n: f"Le department {n}")
    tbs_dept_code = factory.Sequence(lambda n: f"ABC{n}")
    applied_title_en = factory.Sequence(lambda n: f"The department {n} (applied)")
    applied_title_fr = factory.Sequence(lambda n: f"Le department {n} (applied)")
    abbr_en = factory.Sequence(lambda n: f"ABC{n}")
    abbr_fr = factory.Sequence(lambda n: f"ABC{n}")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.dangerously_create(*args, **kwargs)
