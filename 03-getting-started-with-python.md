# Getting Started with Python

## Installing Python

Python is an essential tool for any aspiring programmer, and installing it on your computer is the first step to getting started. The process can vary depending on your operating system. In this section, we'll walk you through the installation steps for Windows, MacOS, and Linux.

### Windows

1. Go to the [Python downloads page](https://www.python.org/downloads/).
2. Click the **"Download Python 3.X.X"** button at the top.
3. When the page shows, scroll down to the bottom and select **"Windows installer (64-bit)"** or **"Windows installer (32-bit)"** depending on your system, it will most likely be **64-bit**.
4. Open the downloaded file and follow the installation instructions.
   1. **IMPORTANT:** Make sure you check the box that says **"Add python.exe to PATH"**, as this will allow you to run Python from the command line.
5. Click **"Install Now"**.
6. Once the installation is complete, open the command prompt and type `python --version` to verify that Python is installed correctly.
7. You should see something like this: `Python 3.X.X`.

#### Manually Add Python to PATH

If you forgot to check the box that says **"Add python.exe to PATH"**, you'll need to add Python to your PATH manually.

1. Open the command prompt and type `python --version`, if you get an error, continue to step 2.
2. Open the start menu and search for **"Python"**.
3. When you see **"Python 3.8 (64-bit)"** or **"Python 3.8 (32-bit)"**, right-click on it and select **"Open file location"**.
   - For **Windows 11**: Within the **Context Menu (Right-click Menu)**, select **"More"** and then **"Open file location"**.
4. A File Explorer window should open, right-click on the shortcut for **"Python 3.8 (64-bit)"** or **"Python 3.8 (32-bit)"** and select **"Open file location"** again.
   - For **Windows 11**: Within the **Context Menu (Right-click Menu)**, select **"More"** and then **"Open file location"**.
5. You should now see a list of files, including one that should be named **"python.exe"**.
6. Now, at the top of the File Explorer window, you should see a rectangular box that should indicate something like either of the following:
   - `This PC > Local Disk (C:) > Program Files > Python > Python3X`.
   - `This PC > Local Disk (C:) > Program Files (x86) > Python > Python3X`.
   - `This PC > Local Disk (C:) > Users > YOUR_USERNAME > AppData > Local > Programs > Python > Python3X`.
   - Replace `YOUR_USERNAME` with your actual username and `X` with the version of Python you installed.
7. Click on the box and copy the directory path to your clipboard, this is the location where Python is installed.
8. Open the start menu and search for **"Edit the system environment variables"**.
9. Click **"Environment Variables..."**.
10. Under **"System variables"**, find the variable named **"Path"** and double-click on it.
11. Click **"New"** and paste the directory path you copied earlier.
12. Click **"OK"**.
13. Click **"OK"** again.
14. Close any/all command prompts that you have open and re-open them.
15. You should now be able to type `python --version` and see something like this: `Python 3.X.X`.
16. If you see `Python 2.X.X` or a different version than you downloaded, then try typing `python3X --version` instead.
    - Replace `X` with the version of Python you installed.
17. If you see `Python 3.X.X`, you're all set!

### MacOS

1. Go to the [Python downloads page](https://www.python.org/downloads/).
2. Click the **"Download Python 3.X.X"** button at the top.
3. When the page shows, scroll down to the bottom and select **"macOS 64-bit installer"**.
4. Open the downloaded file and follow the installation instructions.
5. Once the installation is complete, open the terminal and type `python --version` to verify that Python is installed correctly.
6. You should see something like this: `Python 3.X.X`.
7. If you see `Python 2.X.X`, try typing `python3 --version` instead.
8. If you see `Python 3.X.X`, you're all set!
9. If you see `python: command not found`, you'll need to add Python to your PATH.
   1. Open the terminal and type `nano ~/.bash_profile`.
   2. Add the following line to the file: `export PATH="/Library/Frameworks/Python.framework/Versions/3.X/bin:$PATH"`.
   3. Press `Ctrl + X` to exit, then press `Y` to save the changes.
   4. Close the terminal and open it again.
   5. Type `python --version` to verify that Python is installed correctly.
   6. You should see something like this: `Python 3.X.X`.

### Linux

1. Ensure your system is up-to-date by typing the following in the terminal.
   - Debian/Ubuntu: `sudo apt-get update && sudo apt-get upgrade`
   - Centos/Fedora/RHEL: `sudo yum update && sudo yum upgrade`
   - Arch: `sudo pacman -Syu`
2. Install Python by typing the following in the terminal.
   - Debian/Ubuntu: `sudo apt-get install python3`
   - Centos/Fedora/RHEL: `sudo yum install python3`
   - Arch: `sudo pacman -S python3`
3. Once the installation is complete, open the terminal and type `python --version` to verify that Python is installed correctly.
4. You should see something like this: `Python 3.X.X`.
5. If you see `Python 2.X.X`, try typing `python3 --version` instead.
6. If you see `Python 3.X.X`, you're all set!

## Quickstart Guide

Python is an interpreted programming language, which means that if you want to run Python code, you need to install Python. Unlike compiled languages, Python doesn't need a compiler to translate your code into machine language. Instead, it uses an interpreter. This means that you can write a line of code, and then execute it immediately.

So, there are two methods to run Python code:

1. Write your code in a file, save it, then run it from the command line.
2. Write your code in the Python REPL, which is the Python command line interface.

### Running Python Code

#### Running Python Code in a File

Let's say you wrote some code in a file named `script.py` and you want to run the code. You can do this by opening the command line, ***navigating to the directory where the file is located***, and running the following command:

```bash
python script.py
```

#### Running Python Code in the REPL

The REPL stands for Read-Evaluate-Print-Loop and it is the Python command line interface. This interface is useful for testing short amounts of code because you can write code and see the results immediately without having to write a file.

To run the REPL, open the command line and type the following:
```bash
python
```

You should see something like this:
```bash
Python 3.8.5 (default, Jan 27 2021, 15:41:15)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more
information.
>>>
```

Now you can write any Python code and see the results immediately. For example, if you type `print("Hello, World!")`, you should see the following:
```bash
>>> print("Hello, World!")
Hello, World!
>>>
```

To exit the REPL, type `exit()` and press `Enter`.


## Installing Python

Python is an essential tool for any aspiring programmer, and installing it on your computer is the first step to getting started. The process can vary depending on your operating system. In this section, we'll walk you through the installation steps for Windows, MacOS, and Linux.

### Windows

1. Go to the [Python downloads page](https://www.python.org/downloads/).
2. Click the **"Download Python 3.X.X"** button at the top.
3. When the page shows, scroll down to the bottom and select **"Windows installer (64-bit)"** or **"Windows installer (32-bit)"** depending on your system, it will most likely be **64-bit**.
4. Open the downloaded file and follow the installation instructions.
   1. **IMPORTANT:** Make sure you check the box that says **"Add python.exe to PATH"**, as this will allow you to run Python from the command line.
5. Click **"Install Now"**.
6. Once the installation is complete, open the command prompt and type `python --version` to verify that Python is installed correctly.
7. You should see something like this: `Python 3.X.X`.

#### Manually Add Python to PATH

If you forgot to check the box that says **"Add python.exe to PATH"**, you'll need to add Python to your PATH manually.

1. Open the command prompt and type `python --version`, if you get an error, continue to step 2.
2. Open the start menu and search for **"Python"**.
3. When you see **"Python 3.8 (64-bit)"** or **"Python 3.8 (32-bit)"**, right-click on it and select **"Open file location"**.
   - For **Windows 11**: Within the **Context Menu (Right-click Menu)**, select **"More"** and then **"Open file location"**.
4. A File Explorer window should open, right-click on the shortcut for **"Python 3.8 (64-bit)"** or **"Python 3.8 (32-bit)"** and select **"Open file location"** again.
   - For **Windows 11**: Within the **Context Menu (Right-click Menu)**, select **"More"** and then **"Open file location"**.
5. You should now see a list of files, including one that should be named **"python.exe"**.
6. Now, at the top of the File Explorer window, you should see a rectangular box that should indicate something like either of the following:
   - `This PC > Local Disk (C:) > Program Files > Python > Python3X`.
   - `This PC > Local Disk (C:) > Program Files (x86) > Python > Python3X`.
   - `This PC > Local Disk (C:) > Users > YOUR_USERNAME > AppData > Local > Programs > Python > Python3X`.
   - Replace `YOUR_USERNAME` with your actual username and `X` with the version of Python you installed.
7. Click on the box and copy the directory path to your clipboard, this is the location where Python is installed.
8. Open the start menu and search for **"Edit the system environment variables"**.
9. Click **"Environment Variables..."**.
10. Under **"System variables"**, find the variable named **"Path"** and double-click on it.
11. Click **"New"** and paste the directory path you copied earlier.
12. Click **"OK"**.
13. Click **"OK"** again.
14. Close any/all command prompts that you have open and re-open them.
15. You should now be able to type `python --version` and see something like this: `Python 3.X.X`.
16. If you see `Python 2.X.X` or a different version than you downloaded, then try typing `python3X --version` instead.
    - Replace `X` with the version of Python you installed.
17. If you see `Python 3.X.X`, you're all set!

### MacOS

1. Go to the [Python downloads page](https://www.python.org/downloads/).
2. Click the **"Download Python 3.X.X"** button at the top.
3. When the page shows, scroll down to the bottom and select **"macOS 64-bit installer"**.
4. Open the downloaded file and follow the installation instructions.
5. Once the installation is complete, open the terminal and type `python --version` to verify that Python is installed correctly.
6. You should see something like this: `Python 3.X.X`.
7. If you see `Python 2.X.X`, try typing `python3 --version` instead.
8. If you see `Python 3.X.X`, you're all set!
9. If you see `python: command not found`, you'll need to add Python to your PATH.
   1. Open the terminal and type `nano ~/.bash_profile`.
   2. Add the following line to the file: `export PATH="/Library/Frameworks/Python.framework/Versions/3.X/bin:$PATH"`.
   3. Press `Ctrl + X` to exit, then press `Y` to save the changes.
   4. Close the terminal and open it again.
   5. Type `python --version` to verify that Python is installed correctly.
   6. You should see something like this: `Python 3.X.X`.

### Linux

1. Ensure your system is up-to-date by typing the following in the terminal.
   - Debian/Ubuntu: `sudo apt-get update && sudo apt-get upgrade`
   - Centos/Fedora/RHEL: `sudo yum update && sudo yum upgrade`
   - Arch: `sudo pacman -Syu`
2. Install Python by typing the following in the terminal.
   - Debian/Ubuntu: `sudo apt-get install python3`
   - Centos/Fedora/RHEL: `sudo yum install python3`
   - Arch: `sudo pacman -S python3`
3. Once the installation is complete, open the terminal and type `python --version` to verify that Python is installed correctly.
4. You should see something like this: `Python 3.X.X`.
5. If you see `Python 2.X.X`, try typing `python3 --version` instead.
6. If you see `Python 3.X.X`, you're all set!

## Quickstart Guide

Python is an interpreted programming language, which means that if you want to run Python code, you need to install Python. Unlike compiled languages, Python doesn't need a compiler to translate your code into machine language. Instead, it uses an interpreter. This means that you can write a line of code, and then execute it immediately.

So, there are two methods to run Python code:

1. Write your code in a file, save it, then run it from the command line.
2. Write your code in the Python REPL, which is the Python command line interface.

### Running Python Code in a File

Let's say you wrote some code in a file named `script.py` and you want to run the code. You can do this by opening the command line, ***navigating to the directory where the file is located***, and running the following command:

```bash
python script.py
```

### Running Python Code in the REPL

The **REPL** stands for **Read-Evaluate-Print-Loop** and it is the Python command line interface. This interface is useful for testing short amounts of code because you can write code and see the results immediately without having to write a file.

To run the REPL, open the command line and type the following:
```bash
python
```

You should see something like this:
```bash
Python 3.8.5 (default, Jan 27 2021, 15:41:15)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more
information.
>>>
```

Now you can write any Python code and see the results immediately. For example, if you type `print("Hello, World!")`, you should see the following:
```bash
>>> print("Hello, World!")
Hello, World!
>>>
>>> 1000 + 330 + 7
1337
>>>
```

To exit the REPL, type `exit()` and press `Enter`.


## Installing a Text Editor

Realistically, you do not require any text editor aside from the default text editor your operating system provides, however I highly recommend using recommend using [Visual Studio Code](https://code.visualstudio.com/) for writing Python code.

Mainly since it's free, open-source, and has a lot of great features that make it easy to write code. It's also one of the most popular text editors for writing code, and it's used by many professional developers.

As most "Getting Started" guides for Python would recommend some kind of IDE (Integrated Development Environment) such as [PyCharm](https://www.jetbrains.com/pycharm/), I personally don't recommend using an IDE for writing Python code.

Mainly because IDEs are often bloated with features that you don't need, they can be confusing to use, and they aren't commonly used by professional developers.

### Installing Visual Studio Code

1. Go to the [Visual Studio Code downloads page](https://code.visualstudio.com/download).
2. Click the **"Download for Windows"** button.
3. Open the downloaded file and follow the installation instructions.
4. Once the installation is complete, you should be able to open **Visual Studio Code** from the start menu.
5. Alternatively, you can open the command line and type `code` to open it.

### Installing the Python Extension

1. Open **Visual Studio Code**.
2. Click the **"Extensions"** icon in the left sidebar.
3. Search for the following extensions and click install:
   1. **Python** by Microsoft
   2. **Pylance** by Microsoft
   3. **Remote - SSH** by Microsoft
   4. **indent-rainbow** by oderwat
4. Once installed, you should see a **"Reload Required"** button, click it.
   - If not, then you should be all set!
5. Now you should be able to write and run Python code in **Visual Studio Code**.
6. If you want to open a file in **Visual Studio Code**, there a few ways to do it:
   1. From **Visual Studio Code**, click **"File"** > **"Open File..."** and select the file you want to open.
   2. Alternatively, from the command-line you can type `code FILENAME` to open it.
      - Replace `FILENAME` with the name of the file you want to open.
7. If you want to open the directory where a file is located, you can do the following:
   1. From **Visual Studio Code**, click **"File"** > **"Open Folder..."** and select the directory you want to open.
   2. Alternatively, from the command-line you can type `code .` to open the current directory.

### Writing and Running Python Code

1. Open **Visual Studio Code**.
2. Click **"File"** > **"Open Folder..."** and select the directory you want to open.
3. Click **"File"** > **"New File"** and name it `hello.py`.
4. Type the following code into the file:
   ```python
   print("Hello, World!")
   ```
5. Click **"File"** > **"Save"**.
6. Click **"Terminal"** > **"New Terminal"**.
   - Alternatively, you can press **Ctrl + Shift + \`** or **Ctrl + Shift + \`** to open the terminal.
7. Type `python hello.py` to run the code.
8. You should see the following output:
   ```
   Hello, World!
   ```
9. Congratulations, you've successfully written and run your first Python program!
