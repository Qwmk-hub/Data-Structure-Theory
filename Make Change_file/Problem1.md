Problem 1. 

Write a Python program that can "make change." Your program should take two numbers as input, one that is a monetary amount charged and the other that is a monetary amount given. 
It should then return the number of each kind of coin to give back as change for the difference between the amount given and the amount charged. 
Try to design your program so that it returns as few coins as possible. 
The available kinds of coins are: 500, 100, 50, and 10 won.

거스름돈을 계산하는 Python 프로그램을 작성하세요. 
프로그램은 두 개의 숫자를 입력으로 받아야 합니다. 
첫 번째 숫자는 청구된 금액이고, 두 번째 숫자는 지불된 금액입니다. 
프로그램은 지불된 금액에서 청구된 금액을 뺀 차이를 잔돈으로 반환해야 하며, 가능한 한 적은 동전을 반환하도록 설계해야 합니다. 
사용할 수 있는 동전의 종류는 500원, 100원, 50원, 10원입니다.

Input specification
Two numbers separated by whitespace will be given. 
The first number represents the monetary amount charged, and the other number represents the monetary amount given.

공백으로 구분된 두 개의 숫자가 주어집니다. 첫 번째 숫자는 청구된 금액, 두 번째 숫자는 지불된 금액을 나타냅니다.

Output specification

If it is possible to make change, output 1 to indicate that it is possible, followed by the number of coins returned, starting from 500 won, then 100, 50, and 10 won, each separated by a single whitespace. If it is not possible to make change, then output only -1.

잔돈을 거슬러 줄 수 있는 경우, 1을 출력한 후 반환된 동전의 개수를 순서대로 출력합니다. (500원, 100원, 50원, 10원 순서로 각각 공백으로 구분하여 출력). 잔돈을 거슬러 줄 수 없는 경우 -1만 출력합니다.
