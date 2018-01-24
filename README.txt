before_install:
   - wget https://github.com/mozilla/geckodriver/releases/needed_geckodriver_version
   - mkdir geckodriver && tar zxvf geckodriver_version -C geckodriver
   - export PATH=$PATH:$PWD/geckodriver

File framework/Dictionary.py is settings (env) file. There need to write down your credentials (email and login).
