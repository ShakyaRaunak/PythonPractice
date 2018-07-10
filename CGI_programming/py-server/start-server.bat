:: A batch file does the work of a mediator between you and the command prompt.
:: It is a file – with .bat, .cmd, .btm file extensions containing the CMD commands.
:: When you run a batch file, the commands written in it are executed in the Command Prompt following a serial fashion.
:: Otherwise, these would have to be entered manually line by line.

:: http://fossbytes.com/complete-windows-cmd-commands-list-index/

:: Try this :
:: start cmd /k echo Hello, World!

:: https://fossbytes.com/what-is-a-batch-file-in-windows-how-to-create-a-batch-file/

:: Try this : Administrator privilege is required to execute the following reports.
:: powercfg/energy
:: powercfg/batteryreport
:: pause
:: This creates a battery-report at C:\Windows\System32\battery-report.html

:: Try this :
:: echo off
:: title My Test Batch File
:: :: See the title at the top. And this comment will not appear in the command prompt.
:: echo Test file executed.
:: echo I am too lazy to write commands again and again.
:: pause

:: Start your own python server to handle CGI scripts
start cmd cd CGI_programming\py-server /k python -m http.server --cgi