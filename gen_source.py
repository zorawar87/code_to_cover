#!/usr/bin/python
import os, sys

args = sys.argv
name, title = "",""
date, cl_name = "", "";
header = ""
if len(args) >=3:
    name, title = args[1], args[2]
    #optional
    if len(args) >= 4:
        date = args[3]
        if len(args) == 5:
            cl_name = args[4]
else:
    print "USAGE: {} \"Full Name\" \"Full Title\" [\"Formatted Date\"|null \"Class Name\"]".format(args[0])

if len(args)>=2:
    header += "\documentclass{article}\n\usepackage{amsmath}\n\usepackage[english]{babel}\n\usepackage{fancyhdr}\n\n%% Sets page size and margins\n\usepackage[top=3cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}\n\n\pagestyle{fancy}\n%\lhead{\\today}\n"
    header += "\lhead{"+name+"}\n";

    if cl_name != "" and cl_name != "null":
        header += "\chead{"+cl_name+"}\n"
    else:
        header += "\chead{CPSC-215}\n"

    header += "\\rhead{"+title+"}\n";
    header += "\lfoot{}\n\cfoot{\\thepage}\n\\rfoot{}\n"

    header += "\\title{"+title+"}\n"
    header += "\\author{"+name+"}\n"

    if date != "":
        header += "\date{"+date+"}\n"
    else:
        header += "\date{\\today}\n"

    header += "\\begin{document}\n\section{Cover Page}\n\underline{Yes} I have followed the academic honesty rules as outlined in the course syllabus.\\newline\n\underline{Yes} I have carefully reviewed the details of the assignment.\\newline\n\underline{Yes} I have organized my printed assignment as outlined in the homework handout.\\newline\n\underline{Yes} I have submitted an identical copy of the assignment on Moodle. \\newline\n\underline{Yes} I used pseudocode, flowcharts or a similar tool to develop my solutions. \\newline\n\underline{Yes} I unit tested and integration tested my solutions.\n"
    os.system("touch source.tex");
    with open("source.tex","w") as to:
        to.write(header)


