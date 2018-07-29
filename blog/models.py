from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125,null=False)
    title = models.CharField(max_length=200,null=False)

    def __str__(self):
        return "<Blog:({id},{name},{title})>".format(id=self.id,
                name=self.name,title=self.title)
class Goods(models.Model):
    goodsId = models.BigAutoField(primary_key=True)
    removed = models.BooleanField(default=False)
    email = models.EmailField(null=True)
