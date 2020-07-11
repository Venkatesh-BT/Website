from django.contrib import admin
from home.models import Test
class TestAdmin(admin.ModelAdmin):
	list_display = ('name','age',)

admin.site.register(Test, TestAdmin)

# Register your models here.
