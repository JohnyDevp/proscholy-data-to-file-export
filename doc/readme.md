Data to file export
====

Autor
-----
Jan Holáň, 2022 <br>
Under Creative Commons Licence
 
Files
---
- readme.md - short documentation
- server.py - flask server handling requests

Run
---
In bash on Linux:
<pre>
$ export FLASK_APP=server
$ flask run
</pre>
In PowerShell on Windows:
<pre>
> flask --app server run 
</pre>

Then go to the IP address and port which has been written out in terminal (usually 127.0.0.1:5000). For detailed usage continue
below.

Description of usage
---

Example
---
<pre>
</pre>

Operating system differences
---
Both platforms requires all neccessary packages to be installed, so make yourself sure that this is done. (if you start the app, it will show you what package is currently missing - you will probably have to do this start-install process more times) <br>
If you are on:
- Windows - find every comment <b>WINDOWS</b>, uncomment the next lines, which are marked and comment each block of code marked with word <b>LINUX</b>. Make sure that every line you uncomment make sense considering your personal PC setup (especially paths).
- Linux - change words <b>WINDOWS</b> and <b>LINUX</b> and do the steps written above

Exceptions
---
When any exception occurs warning appears usually in web browser, sometimes also the description of it is shown in terminal on server. <br>
Mistakes or errors considering parameters are left without any warning.
