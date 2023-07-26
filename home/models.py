from django.db import models

# Create your models here.
class DanhMuc(models.Model):
    DanhMuc_id= models.AutoField(primary_key=True)
    TenDM= models.CharField(max_length=50,null=False)

def __str__(self):
    return f"{self.DanhMuc_id},{self.TenDM}"
