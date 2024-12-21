# Getting Started with Jupyter Notebooks

Aside from the fact that this repository is built atop of Jupyter notebooks, using notebooks as your own method of tracking your work and progress is a great way to get started with Python. They allow you to write and run Python code in your web browser, without having to install anything on your computer. 

In this section, we'll walk you through the process of creating a Jupyter Notebook and running some basic Python code.

## What is it?

Jupyter Notebooks are a great way to get started with Python. They allow you to write and run Python code in your web browser, without having to install anything on your computer. In this section, we'll walk you through the process of creating a Jupyter Notebook and running some basic Python code.

## Installation

If you want to install Jupyter Notebooks on your own computer, you can do so by following the instructions below.

### Windows

1. Open the start menu and search for **"Command Prompt"**.
2. Right-click on **"Command Prompt"** and select **"Run as administrator"**.
3. Type `python -m pip install jupyter` and press `Enter`.
4. Once the installation is complete, type `python -m jupyter --version` and press `Enter`.
5. You should see something like this: `jupyter core     : X.X.X`.
6. If you do see something like this, you're all set!

### MacOS

1. Open a new terminal window by pressing `Command + Space` and typing **"Terminal"**.
2. Type `python -m pip install jupyter` and press `Enter`.
3. Once the installation is complete, type `python -m jupyter --version` and press `Enter`.
4. You should see something like this: `jupyter core     : X.X.X`.
5. If you do see something like this, you're all set!

### Linux

1. Open a new terminal window by pressing `Ctrl + Alt + T`.
2. Type `python -m pip install jupyter` and press `Enter`.
3. Once the installation is complete, type `python -m jupyter --version` and press `Enter`.
4. You should see something like this: `jupyter core     : X.X.X`.
5. If you do see something like this, you're all set!

## Creating a Notebook

First let's create a new directory for your notebook:
1. From your command prompt or terminal, navigate to your Desktop:
   - Windows/MacOS/Linux: `cd Desktop`
2. Now, let's create a new directory for your notebook:
   - Windows/MacOS/Linux: `mkdir my-notebook`
   - Replace `my-notebook` with whatever you want to name your notebook.
3. Now, let's navigate to the directory we just created:
   - Windows/MacOS/Linux: `cd my-notebook`
   - Replace `my-notebook` with whatever you named your notebook.

Now, let's open the notebook:
1. From your command prompt or terminal, from your notebook directory, type the following:
   ```
   python -m jupyter notebook
   ```
2. Your web browser should open to a page for your notebook.
3. If it doesn't, open your web browser and go to [http://localhost:8888](http://localhost:8888).
4. Click **"New"** and select **"Python 3"**.
5. You should now see a new notebook with a cell that says **"In [ ]:"**.
6. Congratz! You've just created your first Jupyter Notebook!

## Running Code

Now that you've created your first Jupyter Notebook, let's run some code!

1. Click on the cell that says **"In [ ]:"**.
2. Type `print("Hello, World!")`.
3. Press `Shift + Enter` to run the cell.
4. You should see `Hello, World!` printed below the cell.
5. Congratz! You've just run your first Python program!

## Saving Your Notebook

Now that you've created your first Jupyter Notebook and run some code, let's save it!

1. Click on the **"File"** menu at the top of the notebook.
2. Click on **"Save and Checkpoint"**.
3. You should see a message that says **"Last Checkpoint: X minutes ago"**.
4. Congratz! You've just saved your first Jupyter Notebook!

## Closing Your Notebook

Now that you've created your first Jupyter Notebook, run some code, and saved it, let's close it!
1. Click on the **"File"** menu at the top of the notebook.
2. Click on **"Close and Halt"**.
3. You should see a message that says **"Are you sure you want to close this tab?"**.
4. Click **"OK"**.
5. Congratz! You've just closed your first Jupyter Notebook!
6. If you want to open it again, just follow the steps in the **"Running Code"** section above.

## Jupyter Basics

Now that you've created your first Jupyter Notebook, run some code, saved it, and closed it, let's learn some basics about Jupyter Notebooks!

### What is a cell?

A cell is a block of code that can be run independently from other cells. Cells can contain any valid Python code, including functions, classes, and variables. Cells can also contain text, which is useful for documenting your code.

### How do I run a cell?

1. Click on the cell that you want to run.
2. Press `Shift + Enter` to run the cell.
3. You should see the output of the cell below the cell.
4. You can also use the **"Run"** button at the top of the notebook to run the currently selected cell.
5. You can also use the keyboard shortcut `Ctrl + Enter` to run the currently selected cell.
6. You can also use the keyboard shortcut `Alt + Enter` to run the currently selected cell and create a new cell below it.

### How do I edit a cell?

1. Click on the cell that you want to edit.
2. You should see a cursor appear in the cell.
3. You can now edit the cell as you would any other text file.
4. You can also use the **"Edit"** button at the top of the notebook to edit the currently selected cell.
5. For Markdown cells, to save your changes, press `Ctrl + Enter` or `Shift + Enter`.
6. For Code cells, to save your changes, press `Shift + Enter`.

### How do I delete a cell?

1. Click on the cell that you want to delete.
2. You should see a trash can icon appear in the top right corner of the cell.
3. Click on the trash can icon to delete the cell.
4. You can also use the **"Edit"** button at the top of the notebook to delete the currently selected cell.
5. You can also use the keyboard shortcut `D` twice to delete the currently selected cell.

### How do I move a cell?

1. Click on the cell that you want to move.
2. You should see a handle appear in the top left corner of the cell.
3. Click and drag the handle to move the cell.
4. You can also use the **"Edit"** button at the top of the notebook to move the currently selected cell.

### How do I add a cell above or below the current cell?

1. Select the cell that you want to add a cell above or below.
2. You should have two options for creating new cells:
   - To create a new cell above the currently selected cell, click on the `+` icon with an outlined box below the `+`.
   - To create a new cell below the currently selected cell, click on the `+` icon with an outlined box above the `+`.
3. You should now see a new cell above or below the currently selected cell.
4. You can also use the keyboard shortcuts `A` and `B` to create new cells above and below the currently selected cell, respectively.
5. You can also use the keyboard shortcuts `Ctrl + Shift + -` and `Ctrl + Shift + +` to split the currently selected cell into two cells.
