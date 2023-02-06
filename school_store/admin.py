from django.contrib import admin
from . models import FormData,Material,Department,Purpose,Course
# Register your models here.

admin.site.register(FormData)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(Purpose)