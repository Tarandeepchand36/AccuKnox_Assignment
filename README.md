# AccuKnox_Task
Topic: Django Signals

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
Explaination: Django signals are a mechanism that allows different parts of a Django application to communicate and respond to events or actions that occur within the application.

By default, Django signals are executed synchronously. This means that when a signal is triggered, the associated signal handlers (i.e., the functions that respond to the signal) are executed immediately within the same thread and request context as the sender.
