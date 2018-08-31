from distutils.core import setup

setup(name='PyContacts',
      version='1.0',
      description='Create Contacts in YAML file',
      author='Aakash Khatri',
      author_email='akhatri@campus.uni-paderborn.de',
      packages=['pycontacts'],
      package_dir={'pycontacts': 'src/pycontacts'},
      package_data={'pycontacts': ['data/*.yaml','data/*.txt']}
     )