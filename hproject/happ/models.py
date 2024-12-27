from django.db import models

# Create your models here.
class Bus(models.Model):
    sid= models.IntegerField()
    sname= models.CharField(max_length=30)
    stamil= models.IntegerField()
    senglish= models.IntegerField()
    smaths= models.IntegerField()
    sscience= models.IntegerField()
    ssocial= models.IntegerField()
    class Meta:
        db_table = "marklist"
