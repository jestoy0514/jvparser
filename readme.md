##JVParser

####What is it?

JVParser is a python module created to be able to calculate
mathematical expressions in form of a string like those of 
an eval function without importing any additional module.

####Installation

Extract the archive and point to the location of *setup.py*
and then execute the code below.

`juan@juan-desktop:~/jvparser-1.3$ python3 setup.py install`

####How to use?

```Python
from jvparser import jvparser`
math_exp = '4+5*2-3'
data = jvparser(math_exp)
print(data)
11.0
```

####License

Please find the file license.

####Contact

* E-mail 1: *jessie@jvaolazo.net76.net*
* E-mail 2: *jestoy.olazo@gmail.com*