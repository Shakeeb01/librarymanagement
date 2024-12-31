from django.contrib import admin
from .models import Book,StudentExtra,IssuedBook

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = [] # here we will pass the list of model fields that we want to display in admin panel.
    list_editable = [] # this will give the permission to edit specific fields.
    
admin.site.register(Book, BookAdmin)


class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)


class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookAdmin)
