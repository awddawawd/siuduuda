n=5
from importlib import reload
import screenshot
import time
time.sleep(5)
import sudoku_scanner
import solver
import os
os.remove("temp.txt")
os.remove("answer.txt")
import last
os.remove("final_answer.txt")
while n == 5:
	time.sleep(3)
	reload(screenshot)
	time.sleep(1)
	reload(sudoku_scanner)
	reload(solver)
	reload(last)
	print("done")