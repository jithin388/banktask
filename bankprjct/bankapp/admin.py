from django.contrib import admin
from .models import place
from. models import Category
# Register your models here.
class PlacesAdmin(admin.ModelAdmin):
    
     list_dislplay= ['name','slug']
     prepopulated_fields= {'slug':('name',)}
admin.site.register(place,PlacesAdmin)

admin.site.register(Category)