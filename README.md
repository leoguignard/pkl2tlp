# pkl2tlp

Small script to convert a pickle output from the output of our paper [Contact-dependent cell communications drive morphological invariance during ascidian embryogenesis](https://www.biorxiv.org/content/early/2018/02/22/238741.1 "ASTEC") into a [tulip](http://tulip.labri.fr/TulipDrupal/ "tulip") friendly file

## Content
- README.md: this file
- setup.py: install script
- pkl2tlp.py: the converting script

## Dependecy
- cPickle

## Install
To install the script you can run the following command:
```shell
python setup.py install --user
```
Note that since it is just a small script that do not have dependecy, if you do not need to access it from "anywhere" on your computer, the installation part using ```setup.py``` is not necessary.

## Typical usage
Once install with the previous command, or from the folder containing the script, you can run the script as follow:
```shell
pkl2tlp.py -i path/to/input.pkl -o path/to/output.tlp
```
or if you want to print the "help", run 
```shell
pkl2tlp.py -h
```