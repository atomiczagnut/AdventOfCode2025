# Thought Process
My initial thought was to create an array that contained the numbers 0-99, then I realized that would be redundant.
Instead, I made a variable called **pointer** that would track where the dial was.
I also made a **zero_times** counter and initalized it to 0. 

I know global variables aren't best practice, but for a tiny script like this they are the simplest solution.

The **turn_dial** function strips the input of it's left or right, and returns the value as a positive or negative.
Again, I would normally separate these concerns into two functions, but this is the quick and easy way.

Then we glue it all together by reading each line of the file and incrementing the **zero_times** counter.

Easy peasy, right?

## Challenges
Even with little scripts, there are always bugs!

The main headache was an off-by-one error I seemed to keep getting.  Did my modulos need to be 100 instead of 99?
That didn't fix it.

Finally, after sticking a bunch of print messages into my code, and running it against the example data, I realized my problem:
I needed to add a final modulo wrapper around the function call!
