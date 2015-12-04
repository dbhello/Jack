from django.contrib import admin
from management.models import *


class BookAdmin(admin.ModelAdmin):
	list_display = ('bid', 'title', 'author', 'noofcopies', 'pubid', 'secid')

admin.site.register(Book)
admin.site.register(Img)
admin.site.register(Reservation)
admin.site.register(BorrowInfo)
admin.site.register(BookEval)
admin.site.register(Publisher)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(BookCopy)
admin.site.register(Author)
admin.site.register(Student)
admin.site.register(Librarian)
