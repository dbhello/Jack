#coding:utf8
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


class Student(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 16)
    phone = models.CharField(max_length = 11)
    address = models.CharField(max_length = 300)
    major = models.CharField(max_length=50)
    education = models.CharField(max_length=30)
    politics = models.CharField(max_length = 30)
    academy = models.CharField(max_length = 50)
    permission = models.IntegerField()

    def __unicode__(self):
        return self.name

class Librarian(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 16)
    phone = models.CharField(max_length = 11)
    address = models.CharField(max_length = 300)
    permission = models.IntegerField()
    def __unicode__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __unicode__(self):
        return self.name

class Book(models.Model):
    isbn = models.CharField(max_length = 200,primary_key = True)
    call_number = models.CharField(max_length=200)
    name = models.CharField(max_length = 128)
    price = models.FloatField()
    author = models.ManyToManyField(Author)
    pubDate = models.DateField()
    typ = models.CharField(max_length = 128)
    desc = models.CharField(max_length=1000)
    copies_num = models.IntegerField()
    borrowed_num = models.IntegerField()
    publisher = models.ForeignKey(Publisher)

    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class BookCopy(models.Model):
    book = models.ForeignKey(Book)
    copyindex = models.IntegerField()
    barcode = models.CharField(max_length=30)
    STATUS_CHOICE = (('borrowed',u'已借出'),('available',u'外借本'))
    LOC_CHOICE = (('east',u'东校区流通'),('north',u'北校区流通'),('south',u'南校区流通'))
    status = models.CharField(max_length=10,choices=STATUS_CHOICE,default='available')
    collection_loc = models.CharField(max_length=10,choices=LOC_CHOICE,default='east')

    class META:
        ordering = ['copyindex']

    def __unicode__(self):
        return u'%s %s' % (self.copyindex,self.book.name)

class Notification(models.Model):
    librarian = models.ForeignKey(Librarian)
    time = models.DateTimeField()
    content = models.TextField()

class Message(models.Model):
    msg_content = models.TextField()
    msg_time = models.DateTimeField()
    student = models.ForeignKey(Student)

class Img(models.Model):
    name = models.CharField(max_length = 128)
    desc = models.TextField()
    img = models.ImageField(upload_to = 'image')
    book = models.ForeignKey(Book)
    class META:
        ordering = ['name']
    def __unicode__(self):
        return self.name

class Reservation(models.Model):
    bookcopy = models.ForeignKey(BookCopy)
    user = models.ForeignKey(Student)
    resDate = models.DateField()
    dueDate = models.DateField()
    STATUS_CHOICE = ((u"满足",u"满足"),(u"处理中",u"处理中"))
    status = models.CharField(max_length=40,choices=STATUS_CHOICE,default=u"处理中")
    LOC_CHOICE = ((u'东校区流通',u'东校区流通'),(u'北校区流通',u'北校区流通'),(u'南校区流通',u'南校区流通'))
    loc = models.CharField(max_length=30,choices=LOC_CHOICE,default='east')
    def __unicode__(self):
        return self.bookcopy.book.name

class BorrowInfo(models.Model):
    bookcopy=models.ForeignKey(BookCopy)
    user=models.ForeignKey(Student)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True,blank=True)
    def __unicode__(self):
        return self.bookcopy.book.name

class BookEval(models.Model):
    book=models.ForeignKey(Book)
    user=models.ForeignKey(Student)
    RATE_CHOICE = (
                   ('excellent','Excellent'),
                   ('good','Good'),
                   ('average','Average'),
                   ('fair','Fair'),
                   ('poor','Poor'),
                   )
    rate = models.CharField(max_length=2,choices=RATE_CHOICE,default='excellent')
    evalDesc = models.CharField(max_length=500)
    evalDate = models.DateField()

    def __unicode__(self):
        return self.book.name





