from django.contrib import admin
from thelibrary.models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
	fields = ['isbn','author','title']

admin.site.register(Book, BookAdmin)

admin.site.register(Person)


admin.site.register(CheckedOut)
