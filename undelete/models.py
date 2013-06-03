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
		if deleted_at or really:
			super(Trashable, self).delete(*args, *kwargs)
		else:
			self.deleted_at = datetime.now()
			self.save()

	def restore(self):
		self.deleted_at = None
	
	class Meta:
		abstract = True
