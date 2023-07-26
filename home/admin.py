from django.contrib import admin
from .models import DanhMuc
# Register your models here.
class DanhMucADmin(admin.ModelAdmin):
   list_display= ('DanhMuc_id','TenDM')
   search_fields= ['TenDM']
   list_filter= ('DanhMuc_id','TenDM')
# đưa bảng Danh mục hiển thị trang admin
admin.site.register(DanhMuc,DanhMucADmin)