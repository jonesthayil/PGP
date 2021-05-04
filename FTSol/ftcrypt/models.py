from django.db import models

# Create your models here.


class FTCRYPT(models.Model):
	postfile = models.FileField()
	insertedon = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.postfile)

	class Meta:
		db_table = 'mst_postfile'
		verbose_name = 'Post File'
		verbose_name_plural = 'Post Files'
		ordering = ["-insertedon"]
