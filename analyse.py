#!/usr/bin/python
import os, sys

args = sys.argv
args.pop(0);

Dir = "./out/"

def prep(line, is_method):
  if is_method == True:
    print "\tclas: "+line
    s = "\\subsection{"+line+"}\n\underline{Yes} The class follows the requirements outlined in the assignment. \\\\\n\underline{Yes} The class is properly documented and commented.\n\\newline\\\\\n\underline{Yes} The class compiles, works according to the specifications, and passed correctness testing.\\newline\n\underline{N/A} The class compiles but does not work according to the specifications. \n\\newline\n\underline{N/A} The class does not compile.\n\\newline\n\n Other Comments: None\n\n"
  else:
    print "\tmeth: "+ line
    s = "\hspace*{1cm}\\subsection{"+line+"}\n\hspace*{1cm}\underline{Yes} The method follows the requirements outlined in the assignment.\n\\newline\n\hspace*{1cm}\underline{Yes} The method is properly documented and commented.\n\\newline\n\hspace*{1cm}\underline{Yes} The method compiles, works according to the specifications, and passed correctness testing.\n\\newline\n\hspace*{1cm}\underline{N/A} The method compiles but does not work according to the specifications.\n\\newline\n\hspace*{1cm}\underline{N/A} The method does not compile.\n\\newline\n\hspace*{1cm}Other Comments: None\n\n"
  return s

def write_class_meth_signat(i):
  for l in i:
    if "public" in l or "private" in l:
      #print "TEST" +l,
      if "class" in l:
        o.write(prep(l.strip()[:l.index("{")-1],True))
      elif ")" in l:
        o.write(prep(l.strip()[:l.index(")")-1],False))
      else:
          print "\tNOT WRITTEN: "+l

def print_class_meth_signat(i):
    for l in i:
      if "public" in l or "private" in l:
        #print "TEST" +l,
        if "class" in l:
          print l.strip()[:l.index("{")-1]
        elif ")" in l:
          print l.strip()[:l.index(")")-1]
        else:
          print "NOT WRITTEN: "+l

def write_header(to):
  with open("source.tex","r") as s:
    for l in s:
      to.write(l);

def write_close(to):
    to.write("\end{document}");

if __name__ == "__main__":
  os.system("rm -r "+Dir)
  os.system("mkdir -p "+Dir)
  with open(Dir+"main.tex", "w") as o:
    write_header(o)
    for f in args:
      print "OPENING FILE: "+f
      with open(f, "r") as i:
        write_class_meth_signat(i)
    write_close(o)
  os.system("pdflatex -output-directory "+Dir+" "+ Dir+"main.tex")


