Data Science
============

My personal tests with data science

Copyright (c) 2019 by Nils Magnus (magnus@linuxtag.org)

Licensed under the GPLv2.

Project 01 is a primer into Pandas and the depending Python libraries. It includes a sample dataset that measured some WLAN activities and can be used as a medium sized, time seried example. It has no specific meaning.

Installation
------------

To replay this project, install the Debian packages in `debpackages.txt` (I didn't figure out how to do that inside a virtual env) with `apt`, create a virtualenv, and finally install the packages listed in `requirements.txt`.

```bash
virtualenv -p python3.5 datascience
source datascience/bin/activate
< debpackages.txt while read package; do apt install $package; done
pip -f ./requirements.txt
```

Configuration
-------------

Matplotlib can be configured to different backends. On my local Ubuntu system I used the Tk backend, which I installed via `apt`. Your mileage may vary.

Operations
----------

```bash
python run.py
```
