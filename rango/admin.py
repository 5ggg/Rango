from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    # why this class should be ahead of the register....


admin.site.register(Category)
admin.site.register(Page, PageAdmin)





