from django.db import models

class Job_Account(models.Model):
    User_account = models.CharField(max_length=30,unique=True)
    User_password = models.CharField(max_length=20)
    User_name = models.CharField(max_length=20)
    User_number = models.CharField(max_length=20,unique=True)
    User_post = models.CharField(max_length=10,unique=True)
# Create your models here.
class Job_Log(models.Model):
    flag = ((1,'已完成任务'),(2,'主任务'),(3,'子任务'),(4,'下阶段任务'))
    a = 1
    level = []
    while a <= 20:
        b = str(int(a * 0.05 * 100)) + '%'
        level.append((a,b))
        a += 1
    level = tuple (level)
    Job_useraccount = models.CharField(max_length=30,unique=True)
    Job_flag = models.IntegerField(choices=flag)
    Job_name = models.CharField(max_length=30,unique=True)
    Job_finish_date = models.IntegerField()
    Job_begin_date = models.IntegerField()
    Job_over_date = models.IntegerField()
    Job_level = models.IntegerField(choices=level)
    Job_introduce = models.TextField()

class Job_Milepost(models.Model):
    Milepost_date = models.IntegerField()
    Milepost_content = models.TextField()

class Job_Log_Main(models.Model):
    a = 1
    level = []
    while a <= 20:
        b = str(int(a * 0.05 * 100)) + '%'
        level.append((a, b))
        a += 1
    level = tuple(level)
    Main_useraccount = models.CharField(max_length=30,unique=True)
    Main_name = models.CharField(max_length=30,unique=True)
    Main_begin_date = models.IntegerField()
    Main_finish_date = models.IntegerField()
    Main_level = models.IntegerField(choices=level)
    Main_introduce = models.TextField()

class Job_Log_Secondly(models.Model):
    a = 1
    level = []
    while a <= 20:
        b = str(int(a * 0.05 * 100)) + '%'
        level.append((a, b))
        a += 1
    level = tuple(level)
    Secondly_useraccount = models.CharField(max_length=30,unique=True)
    Secondly_name = models.CharField(max_length=30,unique=True)
    Secondly_begin_date = models.IntegerField()
    Secondly_finish_date = models.IntegerField()
    Secondly_level = models.IntegerField(choices=level)
    Secondly_introduce = models.TextField()

class Job_Log_Next(models.Model):
    Next_useraccount = models.CharField(max_length=30,unique=True)
    Next_name = models.CharField(max_length=30,unique=True)
    Next_begin_date = models.IntegerField()
    Next_introduce = models.TextField()
