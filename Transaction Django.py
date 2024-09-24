# models.py
from django.db import models, transaction                       # This imports the core Django ORM (models) and the transaction module to handle database transactions.
from django.db.models.signals import pre_save, post_save        #This imports the pre_save and post_save signals
from django.dispatch import receiver                            #This imports the receiver decorator, which is used to connect signal handlers to signals.

class MyModel(models.Model):
    name = models.CharField(max_length=100)

#This decorator connects the function my_signal_handler to the pre_save signal for the MyModel class. 
# This means the function will be called just before a MyModel instance is saved to the database.

@receiver(pre_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Inside pre_save signal handler")                     # Outputs a message indicating that the signal handler is executing.
    instance.name = "Updated by Signal"                         #This line modifies the name attribute of the instance to "Updated by Signal".

# Testing in Django shell
from myapp.models import MyModel                                #Imports the MyModel class so it can be used to create an instance and test the signal.
from django.db import transaction                               #Imports the transaction module for managing database transactions.

try:
    with transaction.atomic():                                  #Initiates a transaction block. All operations within this block are treated as a single transaction. If any operation fails, all changes will be rolled back.
        my_instance = MyModel(name="Test")
        my_instance.save()                                      # This triggers the pre_save signal
     # Force a transaction failure by raising an exception
        raise Exception("Force rollback")
except:
    print("Transaction rolled back")                            #This line prints a message indicating that the transaction was rolled back due to the exception raised.

# Check if the database has saved the changes
print(MyModel.objects.all())

#This line queries the database for all instances of MyModel. Since the transaction was rolled back (due to the raised exception), no changes were committed to the database.

#Expected Output: The output will show an empty queryset (<QuerySet []>), indicating that the instance was not saved.

#CONCLUSION
#This step-by-step process demonstrates how Django models, signals, 
# and transactions work together, particularly in handling cases where you might want to roll back changes due to errors or exceptions.