"""
Command line tool for using the sudoku-scanner on saved images
"""
import os
import argparse
from sudoku import Sudoku

x = 1

def scan(img_path):
    """Scans image and outputs predictions."""
    sudoku = Sudoku(img_path)
    sudoku.process()
    sudoku.predict()
    return sudoku






sudoku = scan('C:\\Users\\A\\Desktop\\sdk\\sudoku-scanner-master\\src\\screenshot.jpg')
if x == 2:
    print(NO)
    #with open(args.output, 'w') as f:
        #f.write(str(sudoku.predictions))
else:
    print(sudoku)
    f = open("1.txt", "w")
    f.write(str(sudoku))
    f.close()
    f = open("1.txt", "r")
    finale = open("temp.txt", "w")
    data = f.read()
    data = data.replace(" ", "")
    finale.write(data)
    f.close()
    finale.close()
    os.remove("1.txt")
