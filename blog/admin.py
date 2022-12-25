from django.contrib import admin
from blog.models import Post, Category, Image
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
