## Pycontacts

Pycontacts is a Python application that uses Python's `argparse` library to let users add contacts directly from terminal to a Yaml file.

### REQUIREMENTS

* Python (2.7.14 or higher)
* PyYaml



For the installation of PyYaml run the following in your terminal
```
pip install PyYaml
```

Further information on PyYaml can be found here `https://pyyaml.org/wiki/PyYAML`


### INSTALL

If you have downloaded the source code:

    python setup.py install

### DESCRIPTION

Once you have downloaded the source code, you can do following three things:
 * Add new contacts
 * Search for a contact by full name
 * View all the contacts

Pycontacts supports five commands in terminal:  `--add, --number, --email, --list, --show`

 
* For adding new contacts
```
py-contacts.py --add Aakash Khatri --number 0919910131964 --email akhatri@gmail.com
```

* For searching a contact by full name
```
py-contacts.py --show Aakash Khatri
```

* For viewing all the contacts in file
```
py-contacts.py --list
```

## AUTHOR

* **Aakash Khatri** - *Initial work* - [arjox](https://github.com/ajrox)

