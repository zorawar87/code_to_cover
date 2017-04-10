#!/usr/bin/python
import os, sys

print "========Prep========"
name = input("Author Name(s) ")
title = input("Title of Assignment ")
cl_name = input("Class/Affiliation (<enter> for CPSC-215) ")
date = input("Date to print (<enter> for today) ")

if (len(name)>1 and len(title)>1):
    os.system("./gen_source %s %s %s %s 12>/dev/null".format(name,title,date,cl_name))
    print "Source Generated"



