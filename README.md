# KLC-Code-Words
My copy of the KLC Code Words with Python project.

## Goals of the project
The learning objectives for participants are as follows:

* identify key components of secure passwords
* work as a group to divide the example password generator project into at least 2 simplified parts to make the programming more manageable
* create a password generator with Python that uses variables and lists to track and store data
* correctly identify the application of key coding concepts within the password generator project
* collaborate to propose solutions to bugs encountered throughout the workshop

## Key Coding Concepts

### Algorithms
A set of step-by-step instructions to follow in order to solve a problem.
We all follow a similar algorithm when brushing our teeth.
We put toothpaste on our toothbrushes, scrub our teeth with said toothbrush, and then rinse our mouths.

### Sequence
An ordered series of steps for a task; computers read and perform tasks in order from top to bottom.
Think back to our algorithm example.
Have you ever tried to brush your teeth by rinsing your mouth first and scrubbing your teeth with toothpaste second?
The sequence or order of the commands matters!

### Output
Information the computer supplies to its user.
After we press a letter and number (e.g. A5) in a vending machine, for example, the machine releases our treat as the output.

### Variables
Allow us to store a single piece of information.
We can think of a variable as our piggy bank or wallet, which stores our money.
The amount of money we have can change depending on our actions.
Did we pay rent or go on a shopping spree?
If we want to know how much money we have at any given time, we just need to look inside our piggy bank or wallet.

### Lists (Arrays)
A special variable that can store more than one value at a time; items are ordered so that we can access them later.
An array is like a photo album for your last family trip.
The album allows us to store lots of related memories (photos!) in one place.
When we want to look back at these specific memories, we just pull up the photo album.

## Crack Passwords
A simple password cracker that can show how easy it is to generate brute force hacking.
```
from CrackDemPWCLC.getCracking import attack
for p in ["Refrigerating", "13579", "H4CK3R", "W3lc0m3!"]:
    attack(p)
```
