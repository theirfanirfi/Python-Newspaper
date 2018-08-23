from django.db import models

# Create your models here.

class ArticleModel(models.Model):
	article_id = models.AutoField(primary_key=True)
	publish_date = models.CharField(max_length=40,null=True)
	visit_date = models.CharField(max_length=40)
	article_url = models.TextField()

	class Meta:
		db_table = "articleTable"
