# Supercharge your code with Python's 'match' statement

#### Description Page
https://2024.pycon.it/en/event/supercharge-your-code-with-pythons-match-statement

#### Talk
https://www.youtube.com/live/-bpwE60oLZo?si=NximEHE_0mhx3FM0&t=17653





#### How match works in a nutshell
Basically it is more than just if else statements. 
When using match you should not provide just a string or just a value to match, you should provide a pattern of 
the structure.
See the first example for better understanding.

#### example_1:
We are faking get response and using match to print out our response.
For the first case to be executed we need all these conditions to be true:
* value is a tuple;
* tuple has 2 elements inside it;
* the first element of the tuple must be a string and have value "OK";
* the second element in this case can be anything else;

What also happens with the second element is that we are specifying new variable called: 'id'. match will 
capture the value of second element and will assign it to 'id'.

#### example_2:
On this example we are giving a dictionary pattern. Previously it was a tuple pattern.
Key takeaways:
* match will check if it is a dictionary;
* if there is a key named: 'errors' (first case);
* it will capture the value of 'errors' and keep it in new variable 'errors';
* if I understand correctly it does not matter if dictionary pattern has more keys, it is only looking for the ones 
that were provided in that particular case statement;
* second case statement is also using additional condition, which is checked only if the pattern and the keys are all 
matched correctly. This condition is called a guard.

#### example_3:
#### Using match with a custom class.
It also shows the possibility of using 'or' condition by adding '|' followed by a condition.

#### example_4:
#### class matching

#### example_5:
Import case! Whatever is in case statement - it is not a Python code. It is pattern syntax!!!
When you put a variable in case syntax it is used to capture a value.
It does not mean match the string inside this variable. Keep that in mind.

In this particular example there is no pattern, so no matter what is the data the first case will always match. 
And whatever the value it will be put into variable NORTH.

##### To go around this the can use Enum

### Summary
* To make the most of the match statement, we need to recognize the right situation where to use it.
* When all you need is a simple switch-case matching against literals, using if/elif/else is better most of the time.
* As we design the system better, the match statement becomes more useful.