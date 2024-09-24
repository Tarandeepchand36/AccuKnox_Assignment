
from django.db import models                           #This imports Django's models module, which is used to define database models.
from django.db.models.signals import pre_save          #This imports the pre_save signal, which is fired just before a model instance is saved to the database.
from django.dispatch import receiver                   #This imports the receiver decorator, which is used to connect a signal to a handler.
import time                                            #This will help demonstrate how long the signal execution takes.

class MyModel(models.Model):
    name = models.CharField(max_length=100)

#This is a decorator that connects the my_signal_handler function to the pre_save signal of MyModel. 
#This means the function will be executed every time a MyModel instance is about to be saved. 

@receiver(pre_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal started execution.")               #This outputs a message to the console indicating that the signal handler has started execution.
    time.sleep(5)                                    # Simulate a delay of 5 seconds
    print("Signal finished execution.")


 # TESTING CODE
import time
from myapp.models import MyModel

my_instance = MyModel(name="Test")                  #This creates an instance of the MyModel class with the name field set to "Test".

start_time = time.time()
my_instance.save()                                  # This triggers the pre_save signal
end_time = time.time()                              #This captures the current time (in seconds) after the save() operation has completed.

print(f"Save operation took {end_time - start_time} seconds.")

#This prints the total time it took to execute the save() operation, including the time spent in the signal handler.
#The end_time - start_time calculates the difference between the two timestamps, which gives the duration of the save() operation in seconds.
#If the signal handler introduces a 5-second delay (time.sleep(5)), the output should show a value close to 5 seconds.

#CONCLUSION: 
# This code demonstrates that Django signals (in this case, the pre_save signal) are executed synchronously. 
# The save() operation waits for the signal handler to complete before it finishes. 
# This is to  measured the time taken to perform the save() operation, which included a simulated 5-second delay, proving the synchronous execution of signals.