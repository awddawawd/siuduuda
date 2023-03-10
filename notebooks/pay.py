def run_pipeline():
    templates = {
        {
         "cells": [
          {
           "cell_type": "markdown",
           "metadata": {},
           "source": [
            "#### This short notebook shows you how you can see how your own images are processed"
           ]
          },
          {
           "cell_type": "markdown",
           "metadata": {},
           "source": [
            "Imports and adding /src to current PATH"
           ]
          },
          {
           "cell_type": "code",
           "execution_count": 1,
           "metadata": {},
           "outputs": [],
           "source": [
            "import os\n",
            "import sys\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "import cv2\n",
            "%matplotlib inline\n",
            "\n",
            "module_path = os.path.abspath(\n",
            "    os.path.join(os.path.abspath('.'), '../src'))\n",
            "sys.path.insert(0, module_path)"
           ]
          },
          {
           "cell_type": "markdown",
           "metadata": {},
           "source": [
            "Now we can import form /src:"
           ]
          },
          {
           "cell_type": "code",
           "execution_count": null,
           "metadata": {},
           "outputs": [],
           "source": [
            "from sudoku import Sudoku"
           ]
          },
          {
           "cell_type": "markdown",
           "metadata": {},
           "source": [
            "Now we can load any sudoku image you may have lying around:"
           ]
          },
          {
           "cell_type": "code",
           "execution_count": 3,
           "metadata": {},
           "outputs": [],
           "source": [
            "FILE_NAME = '../tests/testing_data/image1000.jpg'  # CHANGE THIS\n",
            "\n",
            "sudoku = Sudoku(FILE_NAME, save_steps=True)\n",
            "sudoku.process()\n",
            "sudoku.predict()"
           ]
          },
          {
           "cell_type": "markdown",
           "metadata": {},
           "source": [
            "And now to save these to your preferred location:"
           ]
          },
          {
           "cell_type": "code",
           "execution_count": 4,
           "metadata": {},
           "outputs": [],
           "source": [
            "FOLDER_NAME = '../images'  # CHANGE THIS (make sure the directory already exists)\n",
            "\n",
            "for i, step in enumerate(sudoku.steps):\n",
            "    filename = f'{FOLDER_NAME}/step{i}.jpg'\n",
            "    cv2.imwrite(filename, step)"
           ]
          }
         ],
         "metadata": {
          "kernelspec": {
           "display_name": "Python 3",
           "language": "python",
           "name": "python3"
          },
          "language_info": {
           "codemirror_mode": {
            "name": "ipython",
            "version": 3
           },
           "file_extension": ".py",
           "mimetype": "text/x-python",
           "name": "python",
           "nbconvert_exporter": "python",
           "pygments_lexer": "ipython3",
           "version": "3.6.3"
          }
         },
         "nbformat": 4,
         "nbformat_minor": 2
        }

    }

    lex = Lexicaliser(templates=templates)
    # FIXME: embedded coordination doesn't work; flatten or fix in simplenlg?
    input_str = 'Play(john, guitar) & Play(paul, guitar) & ' \
                'Play(george, bass) & Play(ringo, drums)'
    sentence = lex(formula_to_rst(expr(input_str)))
    for e in sentence.elements():
        print(repr(e))

    output_str = realise(sentence)
    print(output_str) 

