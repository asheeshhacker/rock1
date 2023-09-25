from django.contrib import admin

# Register your models here.
from .models import game
from .models import postdata
from .models import contdb
class gameadmin(admin.ModelAdmin):
    list_display=('name')
admin.site.register(game)

class postdataadmin(admin.ModelAdmin):
    list_display=('tittle')
admin.site.register(postdata)

class contadmin(admin.ModelAdmin):
    list_display=('name')
admin.site.register(contdb)    