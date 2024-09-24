# AccuKnox_Task
Django Signals

Question 1: By default are django signals executed synchronously or asynchronously?

Explaination: By default, Django signals are executed synchronously. When a signal is triggered, its connected receiver functions run immediately in the same thread, blocking any further execution until they complete. This behavior ensures that any dependent processes can be handled in a predictable manner. You can check this by observing the execution order in your application logs or console output.

When you send a signal, the connected receiver functions are invoked in the order they were connected. The main application thread waits for these functions to finish executing before continuing. This synchronous behavior ensures that any operations dependent on the signal's processing are completed before proceeding.

The provided code snippet demonstrates how to define a signal and its receiver in Django. When a specific action (like creating a user) triggers the signal, the receiver function is executed in the same thread, immediately performing any defined operations (e.g., logging or sending a notification).

You can verify the synchronous execution of signals by running tests where you check the order of execution to see that the receiver completes before any further processing occurs.
