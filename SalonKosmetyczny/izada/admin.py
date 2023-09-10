from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms

class AdminProfile(admin.ModelAdmin):
    readonly_fields = ('date',)
admin.site.register(Offer)
admin.site.register(Aboutus)
# admin.site.register(Blog)
admin.site.register(WorkPictures)

class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = '__all__'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
