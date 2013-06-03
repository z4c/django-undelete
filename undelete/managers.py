from django.db import models
from django.db.models.query import QuerySet

class TrashQuerySet(QuerySet):
    
    def delete(self):
        for item in self.all():
            item.delete()

class NonTrashedManager(models.Manager):
    ''' Query only objects which have not been trashed. '''
    def get_query_set(self):
        return TrashQuerySet(self.model, using=self._db).filter(trashed_at__isnull=True)

class TrashedManager(models.Manager):
    ''' Query only objects which have been trashed. '''
    def get_query_set(self):
        query_set = super(TrashManager, self).get_query_set()
        return query_set.filter(trashed_at__isnull=False)
