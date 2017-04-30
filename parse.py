#!/usr/bin/python
import os, sys

path,filename =  os.path.split(os.path.realpath(__file__))

print "========Prep========"
name = raw_input("Author Name(s): ")
title = raw_input("Title of Assignment: ")
cl_name = raw_input("Class/Affiliation (<enter> for CPSC-215): ")
date = raw_input("Date to print (<enter> for today): ")
cover_files = raw_input("What files do you want to parse? (space separated): ")
output_file = raw_input("Do you want to append the program output? Filename, or no: ")
source_files = raw_input("Do you want to append the program sources? Space separated Filenames, or no: ")

if (len(name)>1 and len(title)>1):
    os.system(path+"/gen_source %s %s %s %s 12>/dev/null".format(name,title,date,cl_name))
    #os.system(path+"/./gen_source.py {} {} {} {}".format(name,title,date,cl_name))
    print "Source Generated"
    os.system(path+"/./analyse.py 1 {} 2 {} 3 {}".format(cover_files, output_file, source_files))
    print "Files parse and tex-ed"

