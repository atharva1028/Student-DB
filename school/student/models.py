from django.db import models
class Sign(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.name

# class Course_data(models.Model):
#     course=models.CharField(max_length=200)
#     fees=models.IntegerField(max_length=200)
#     comment=models.CharField(max_length=250)
#     is_active=models.BooleanField(default=True)

class Course_datas(models.Model):
    course=models.CharField(max_length=200)
    fees=models.CharField(max_length=200)
    comment=models.CharField(max_length=250)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.course




class Add_students(models.Model):
    sname=models.CharField(max_length=200)
    semail=models.EmailField(max_length=200)
    smobile=models.CharField(max_length=10)
    saddress=models.CharField(max_length=250)
    scollege=models.CharField(max_length=250)
    sdegree=models.CharField(max_length=250)
    total_amount=models.IntegerField(max_length=250)
    paid_amount=models.IntegerField(max_length=250)
    due_amount=models.IntegerField(max_length=250)
    scourse=models.ForeignKey(Course_datas, on_delete=models.CASCADE)
    
