from django.db import models


# Create your models here.
class Student(models.Model):
    reg_no = models.CharField(max_length=15, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    rfid = models.CharField(max_length=15, unique=True)
    balance = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " RFID: " + self.rfid

class Meals(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + str(self.price)

class MealsHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    meal = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name + " " + str(self.created_at)