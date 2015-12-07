from django.contrib import admin
from management.models import *



class BookAdmin(admin.ModelAdmin):
	list_display = ('isbn', 'name', 'typ', 'pubDate', 'call_number', 'desc','copies_num','borrowed_num')

class BookCopyAdmin(admin.ModelAdmin):
	list_display = ('barcode','status','collection_loc')

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name','email')

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name','address','website')

class NotificationAdmin(admin.ModelAdmin):
	list_display = ('time','content','librarian')

class ReservationAdmin(admin.ModelAdmin):
	list_display = ('user','resDate','dueDate','status','loc')
	search_fields = ('user',)

class BorrowInfoAdmin(admin.ModelAdmin):
	list_display = ('bookcopy','user','BorrowDate','ReturnDate')
	search_fields = ('user',)


admin.site.register(Student)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Img)
admin.site.register(BookCopy,BookCopyAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(BorrowInfo,BorrowInfoAdmin)
# admin.site.register(BookEval)
# admin.site.register(Message)
# admin.site.register(Librarian)
