from django.contrib import admin

from .models import Category, Music


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}


class musicAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(Music, musicAdmin)
