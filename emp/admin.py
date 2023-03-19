from django.contrib import admin
from .models import Emp, Testimonial

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working', 'emp_id', 'phone')
    # list_filter=('working', 'emp_id')
    # list_editable=('working', 'emp_id')

admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)
