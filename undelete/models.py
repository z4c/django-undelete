from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from undelete.managers import TrashedManager, NonTrashedManager


class Trashable(models.Model):
	deleted_at = models.DateTimeField(_('Trashed'), editable=False,
		blank=True, null=True, db_index=True, default=None)

	objects = NonTrashedManager()
	trash = TrashedManager()

	def delete(self, *args, **kwargs, really=False):
	    if not really:
	        self.deleted_at = datetime.now()
	        self.save()
	    else:
		super(TrashableMixin, self).delete(*args, **kwargs)

	def restore(self):
		self.deleted_at = None
