# NYT Spelling Bee Solver

Simple command-line bot to solve NYT spelling bee games, written in Python

To use:

1. Create and activate your python virtual environment
2. Then run `pip install -r requirements.txt`
3. Then run the app python file 
```
python3 src/app.py
```

Once the menu is opened, you will be prompted to enter the primary letter (this is the letter which is highlighted in a yellow background and in the center of the game). You will then be prompted to enter the secondary letters (the order is unimportant).

After you enter the final letter, the bot will start typing in 3 seconds. You have to switch back to the NYT game and click on the typing cursor before it starts typing! It will type in all of the answers from the dictionary that I used (it may miss some, depending on the list that the NYT uses and it will also definitely type in a bunch that are not on the NYT list).

Have fun using!