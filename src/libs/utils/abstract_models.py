from datetime import datetime
from django.db import models

class BaseFields(models.Model):
	active = models.BooleanField(default = True)
	date_modified = models.DateTimeField(blank = True, null = True, auto_now = True)
	date_created = models.DateTimeField(blank = True, null = True, default = datetime.now(), editable=False)

	class Meta:
		abstract = True