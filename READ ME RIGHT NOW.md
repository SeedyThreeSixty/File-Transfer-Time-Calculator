Name
File Transfer Time Calculator

Version
2.0

##Description
This utility estimates how long it will take for a file transfer, such as an upload, a download or a drive-to-drive transfer, will take based on the size of the data being transferred and the data transfer speed.

##System Requirements
This program supports Windows XP and higher. You must not be running MacOS or Linux, unless you're running the program from its source script. If you're running from source, the accessible_output2 library must be installed in your python3 environment. On Windows, the additional PyWin32 library must be installed. However, if running from binary, all these dependencies have been included, so there's no need to install anything extra. Running from the binary is recommended if you aren't comfortable with running from a source code file, or if you're just not very computer literate.

##How to Run
If running from binary, launch fttc2.exe. If running from the source file, launch fttc2.py. You might have to show file extentions from within your operating system if you don't see .exe or .py at the end of the filename.

##How to Use
1. Type the size of the data you're transferring in megabytes (MB). If the size is presented to you in kilobytes (KB), divide it by 1024 to convert it into megabytes (MB). Or, if it is shown in gigabytes (GB) times by 1024 to convert to megabytes (MB)
2. Type your data transfer speed in megabits (Mb). If the speed is shown to you in megabytes (MB), times it by 8 to convert into megabits (Mb). For example, 5 megabytes (MB) times 8 is equal to 40 megabits (Mb)
3. The result of the calculation will then be spoken aloud by your screen reader. If no screen reader is running, SAPI5 will speak the result. If you have a braille display connected to your computer, and your screen reader sees it, the result will appear on the braille display as well as being spoken aloud.
4. You will then be asked if you want to do another calculation. If you do, type the letter y (lower case) and press enter. If not, type the letter n (lower case) and press enter.

##Advanced Info (for techies only!)
This utility was written in Python 3.4 and compiled using PyInstaller 3.4. The accessible_output2 module, included in the compiled binary package, is used to pipe text output to a screen reader or system speech API. The program can run on both 32-bit (x86) and 64-bit (x64) system architectures.

##Credits
Big shoutout to Destructatron for helping me defeat bugs in the code. This guy is awesome. He's not the best when it comes to Python, but he's come a long way and he's a good friend to have in your life. Follow him on twitter at https://www.twitter.com/destructatron04

Check out my website at https://houseoffireseed.ML
