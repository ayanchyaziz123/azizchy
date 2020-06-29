from django.contrib import admin
from .models import Category, Post, BlogComment


from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)





admin.site.register(Category)
admin.site.register(BlogComment)
admin.site.register(Post)
