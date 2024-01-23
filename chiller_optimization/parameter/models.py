from tkinter import CASCADE
from django.db import models
from home.models import chiller
from .views import readtemp
# create your models here.

ip_address = '192.168.0.1'
db_number = 1
ct_out_address = 9
ch_in_address = 10

class parameter(models.Model):
    chiller_id = models.foreignkey(chiller, default=None, on_delete=models.CASCADE)
    temperature = models.floatfield(diff_temp_value=readtemp(ip_address,db_number, ct_out_address, ch_in_address))
    
    def __str__(self):
        return f"{'self.chiller_id'}, {'self.temperature'}"