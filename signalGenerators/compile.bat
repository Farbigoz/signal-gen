@echo off

g++ -mdll -O -Wall -IC:\Python\Python39-32\include -c KrlGen.cpp
gcc -shared -LC:\Python\Python39-32\libs KrlGen.o -lpython39 -o KrlGen.pyd

del KrlGen.o


pause