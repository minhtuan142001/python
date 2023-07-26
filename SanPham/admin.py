from django.contrib import admin
from .models import SanPham
# Register your models here.
class SanPhamADmin(admin.ModelAdmin):
   list_display= ('SanPham_id','TenSP','GiaTien','Soluonghienco','ThoigianSD')
   search_fields= ['TenSP']
   list_filter= ('SanPham_id','TenSP','GiaTien','Soluonghienco','ThoigianSD')
# đưa bảng Danh mục hiển thị trang admin
admin.site.register(SanPham,SanPhamADmin)