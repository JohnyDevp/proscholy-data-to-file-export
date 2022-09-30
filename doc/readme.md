Data to file export
====

Autor
-----
Jan Holáň, 2022 <br>
Under Creative Commons Licence
 
Files
---
- doc/readme.md - short documentation
- doc/readme.pdf - short documentation for download
- src/requirements.txt - all dependencies
- src/core.py - module handling the whole process of exporting
- src/presentation.py - module for object Presentation, which handling process of creating presentation
- src/rawpdf.py - module for object RawPdf, which handling process of creating pdf text file
- src/props.py - module consisting of helper objects
- server.py - flask server handling requests


Run
---
In bash on Linux: </br>
<i>Maybe would be necessary add the path of src folder to the PYTHONPATH (some imports are from that folder)</i>
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
With exactly composed JSON file send on this server address you can get either presentation or raw pdf file.
The json has three must-have keys - file, display-options, slides
- <b>file</b>
- - something
- <b>display-options</b>
- <b>slides</b>

Example
---
<pre>
</pre>

Operating system differences
---
- Package <b>python-pptx</b> requires one adjustment - in "pptx/compat/__init__.py" is necessary to add <pre>import collections.abc</pre> otherwise
  it will through errors typical for python 3.10. <br>
- Both platforms requires all neccessary packages to be installed, so make yourself sure that this is done. All requirements are included in requirements.txt situated in src folder<br>
If you are on:
- Windows - find every comment <b>WINDOWS</b>, uncomment the next lines, which are marked and comment each block of code marked with word <b>LINUX</b>. Make sure that every line you uncomment make sense considering your personal PC setup (especially paths).
- Linux - change words <b>WINDOWS</b> and <b>LINUX</b> and do the steps written above

Exceptions
---
When any exception occurs warning appears usually in web browser, sometimes also the description of it is shown in terminal on server. <br>
Mistakes or errors considering parameters are left without any warning.
