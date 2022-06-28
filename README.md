# NextPrime
Have the program find prime numbers until the user chooses to stop asking for the next one.

28/06/2022

Today's challenge for QA LTD - Have a program that will find prime numbers until the user chooses to stop asking for the next one.

I was working this out earlier and this was the only method that I could come up with.

The way it works is that it asks the user to input a number. for example, I will pick 99

The program then adds 1, storing the variable (p) and runs through every single number lower than it and checks whether p is divisible by that number with a remainder of 0. If a number comes up (for example, the first run checks against the number 100, which is divisible by 2) then it increments p by 1 and starts again.

This means that for the initial number of 99, there are 209 steps before the program confirms that 101 is prime - roughly 100 for both lines 5 and 6.

If you choose yes for the next step, then it runs from 101, and has another 213 steps before returning 103.

As someone who is quite concerned about the ethics of coding, I recognise that this could be done *MUCH* more efficiently with standard expressions but this was very much about the logic of the programming.

If I were to get much more in the weeds about this, then I might a prior step which asks whether the number being checked is 1 above or below a multiple of 6 and if not, immediately discard it.
