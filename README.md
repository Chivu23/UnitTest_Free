# Some practice with unittest library
## UnitTest_Free

Library that supports the creation of directly runnable tests inside the classes

## How to use UNITTEST:
1. import library: import unittest
2. define a class to contain the tests; the name of this class is important to start with Test and inherit from unittest.TestCase 
3. inside the tests class, we will have access to two special methods:
   - setUp() - here define all the activities that must be performed BEFORE ANY TEST in the respective class. 
   - tearDown() - here define all the activ that must be performed AFTER ANY TEST from  the respective class.
4. define tests : each test is a method of the respective class
- To skip a unittest use "@unittest.skip" after that test
- Running all test files from the terminal: "-m unittest"



