# Advanced parsing of structured data using Python's new match statement

#### Description Page
https://2024.pycon.it/en/event/advanced-parsing-of-structured-data-using-pythons-new-match-statement

#### Talk
https://www.youtube.com/live/-bpwE60oLZo?si=lBnDbQBgov032FpU&t=20990

#### Slides and examples
https://github.com/eGenix/egenix-advanced-match-parsing

### Intro

![Screenshot 2024-06-07 at 16.19.45.png](sreenshots%2FScreenshot%202024-06-07%20at%2016.19.45.png)

* Match object - object you want to match;
* Type pattern - matches the type of object. In this ase if you have a list, then you will go into the first case 
statement;
* Instance pattern - you can match a particular instance. You can also look into that instance and match attributes in 
that instance;
* Sequence - it does not match list, but matches any python sequence. In this particular case a tuple would match this 
case statement.
* Mapping - Do not confuse it with python dictionary. It is looking for any kind of mapping. Worth mentioning that you 
can capture values that are being matched you can put them to variables.
* Wild card - capture data you know nothing about;
* Guard - must match all conditions to go to particular case. In this example: first sequence pattern and later guard 
condition;


![Screenshot 2024-06-07 at 16.42.41.png](sreenshots%2FScreenshot%202024-06-07%20at%2016.42.41.png)

![Screenshot 2024-06-07 at 16.44.27.png](sreenshots%2FScreenshot%202024-06-07%20at%2016.44.27.png)

links:
* https://peps.python.org/pep-0635/
* https://peps.python.org/pep-0636/
* https://peps.python.org/pep-0634/

![Screenshot 2024-06-07 at 16.53.13.png](sreenshots%2FScreenshot%202024-06-07%20at%2016.53.13.png)

![Screenshot 2024-06-07 at 16.58.28.png](sreenshots%2FScreenshot%202024-06-07%20at%2016.58.28.png)

![Screenshot 2024-06-07 at 16.59.36.png](sreenshots%2FScreenshot%202024-06-07%20at%2016.59.36.png)

Test on example_1.
![Screenshot 2024-06-07 at 17.01.14.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.01.14.png)

Test on example_1.
![Screenshot 2024-06-07 at 17.16.15.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.16.15.png)

![Screenshot 2024-06-07 at 17.23.03.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.23.03.png)

![Screenshot 2024-06-07 at 17.23.46.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.23.46.png)

![Screenshot 2024-06-07 at 17.24.36.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.24.36.png)

![Screenshot 2024-06-07 at 17.25.08.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.25.08.png)

![Screenshot 2024-06-07 at 17.25.49.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.25.49.png)

![Screenshot 2024-06-07 at 17.26.29.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.26.29.png)

![Screenshot 2024-06-07 at 17.28.55.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.28.55.png)

![Screenshot 2024-06-07 at 17.29.50.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.29.50.png)

![Screenshot 2024-06-07 at 17.30.36.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.30.36.png)

![Screenshot 2024-06-07 at 17.31.14.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.31.14.png)

![Screenshot 2024-06-07 at 17.31.53.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.31.53.png)

![Screenshot 2024-06-07 at 17.32.24.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.32.24.png)

![Screenshot 2024-06-07 at 17.33.07.png](sreenshots%2FScreenshot%202024-06-07%20at%2017.33.07.png)
