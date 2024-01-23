from django.db import models

# Create your models here.
class chiller(models.Model):
    chiller_id = models.AutoField(primary_key = True)
    chiller_name = models.CharField(max_length=40, null=False)
    
    def __str__(self):
        return f"{'self.chiller_id'},{'self.chiller_name'}"