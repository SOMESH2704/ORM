# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py 

from django.contrib import admin
from .models import Car

admin.site.register(Car)
class caradmin(admin.ModelAdmin):
    list_display = ('car_id','brand','model','year','price')

model.py

from django.db import models

class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.DateField()
    price = models.IntegerField()


```

## OUTPUT

![alt text](<Screenshot 2025-10-03 173916.png>)
![alt text](<Screenshot 2025-10-03 173934.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
