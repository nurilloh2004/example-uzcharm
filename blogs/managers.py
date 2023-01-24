import django
from parler.managers import TranslatableManager, TranslatableQuerySet
from mptt.managers import TreeManager
from mptt.querysets import TreeQuerySet


class CustomMpttQuerySet(TranslatableQuerySet, TreeQuerySet):

    # Optional: make sure the Django 1.7 way of creating managers works.
    def as_manager(cls):
        manager = CustomMpttManager.from_queryset(cls)()
        manager._built_with_as_manager = True
        return manager
    as_manager.queryset_only = True
    as_manager = classmethod(as_manager)


class CustomMpttManager(TreeManager, TranslatableManager):
    queryset_class = CustomMpttQuerySet

    def get_queryset(self):
        # This is the safest way to combine both get_queryset() calls
        # supporting all Django versions and MPTT 0.7.x versions
        return self.queryset_class(self.model, using=self._db).order_by(self.tree_id_attr, self.left_attr)

    if django.VERSION < (1, 6):
        get_query_set = get_queryset
