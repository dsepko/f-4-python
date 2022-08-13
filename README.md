# background
Stumbled upon the F-4 instruction set as I was looking around to see what the minimum required number of instructions to satisfy Turing-completeness was. Of course, OISC exists, but it's really just a mixture of elementary instructions bundled into one. 
# description
A simple interpreter for the F-4 MISC processor whose instruction set is described here: http://www.dakeng.com/misc.htm.

![example](https://user-images.githubusercontent.com/78102845/184464799-898dcdb7-dc77-449d-8f83-9e4066530e25.png)

In the above example image, a very crude check is done to see if the instructions are working as expected. There are 4 instructions: load, store, add, and branch if overflow set. All of these are put into action above, with the final one being a branch from address 7 to 9. Will need to make this look better, and add the ability to load files.

# todo
Add an inteface of some kind. Implement more complex instructions.
