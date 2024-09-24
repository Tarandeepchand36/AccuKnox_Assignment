# models.py

import threading                                
from django.db import models                    
from django.db.models.signals import pre_save
from django.dispatch import receiver

#Here, we define a Django model called MyModel, which will represent a table in the database.
class MyModel(models.Model):
    name = models.CharField(max_length=100)                 #This defines a field called name that can hold string data with a maximum length of 100 characters.

@receiver(pre_save, sender=MyModel)                         # This decorator connects the function my_signal_handler to the pre_save signal for the MyModel class.
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")

#This line prints the name of the current thread where the signal handler is being executed. 
# It will help demonstrate that the signal runs in the same thread as the caller.



# Testing in Django shell
from myapp.models import MyModel                            #This imports the MyModel class from the application named myapp.
import threading

my_instance = MyModel(name="Test")                          #This creates an instance of MyModel with the name field set to "Test".

print(f"Main thread: {threading.current_thread().name}")    
#This prints the name of the main thread before saving the model instance. 
#It allows you to compare it with the thread name printed in the signal handler.

my_instance.save()  # This triggers the pre_save signal


#EXPECTED OUTPUT : Main thread: MainThread as well as Signal thread: MainThread 
# Confirming that the signal runs in the same thread as the caller, which is the main execution thread.

#
