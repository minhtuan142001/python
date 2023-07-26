from django.db import models
from home.models import DanhMuc
# Create your models here.
class SanPham(models.Model):
    SanPham_id= models.AutoField(primary_key=True)
    DanhMuc_id= models.ForeignKey(DanhMuc, default=None, on_delete=models.CASCADE)
    TenSP= models.CharField(max_length=50,null=False)
    GiaTien= models.FloatField()
    Soluonghienco= models.IntegerField()
    ThoigianSD= models.CharField(max_length=50)

def __str__(self):
    return f"{self.SanPham_id},{self.DanhMuc_id},{self.TenSP},{self.GiaTien},{self.Soluonghienco},{self.ThoigianSD}"


