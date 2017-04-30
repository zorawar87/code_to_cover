#!/usr/bin/python
import os, sys

args = list(sys.argv)
args.pop(0);

Dir = "./out/"

def prep(line, is_class):
  if is_class == True:
    print "\tclas: "+line
    s = "\\subsection{"+line+"}\n\underline{Yes} The class follows the requirements outlined in the assignment.\\newline\n\underline{Yes} The class is properly documented and commented.\\newline\n\underline{Yes} The class compiles, works according to the specifications, and passed correctness testing.\\newline\n\underline{N/A} The class compiles but does not work according to the specifications. \\newline\n\underline{N/A} The class does not compile.\\newline\n\n Other Comments: None\n\n"
  else:
    print "\tmeth: "+ line
    s = "\hspace*{1cm}\\subsection{"+line+"}\n\hspace*{1cm}\underline{Yes} The method follows the requirements outlined in the assignment.\n\\newline\n\hspace*{1cm}\underline{Yes} The method is properly documented and commented.\n\\newline\n\hspace*{1cm}\underline{Yes} The method compiles, works according to the specifications, and passed correctness testing.\n\\newline\n\hspace*{1cm}\underline{N/A} The method compiles but does not work according to the specifications.\n\\newline\n\hspace*{1cm}\underline{N/A} The method does not compile.\n\\newline\n\hspace*{1cm}Other Comments: None\n\n"
  return s

def write_class_meth_signat(src,to):
  for l in src:
    if "public" in l or "private" in l:
      if "class" in l:
        to.write(prep(l.strip()[:l.index("{")-1],True))
      elif ")" in l:
        to.write(prep(l.strip()[:l.index(")")-1],False))
      else:
          print "\tNOT WRITTEN: "+l

def print_class_meth_signat(i):
    for l in i:
      if "public" in l or "private" in l:
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

def write_output(src, to):
    to.write("\\newpage\n\\section{Output}\n\\begin{verbatim}")
    for l in s:
      to.write(l);
    to.write("\\end{verbatim}\n\n")

def write_source(src, to):
    to.write("\\newpage\n\\section{"+src.name+"}\n\\begin{verbatim}")
    for l in src:
      to.write(l);
    to.write("\\end{verbatim}\n\n")

def write_close(to):
    to.write("\end{document}");

if __name__ == "__main__":
  os.system("rm -r "+Dir)
  os.system("mkdir -p "+Dir)
  with open(Dir+"main.tex", "w") as to:
    write_header(to)
    print 'header print'
    print args
    print
    if(args[0]=='1'):
        args.pop(0);
        for f in args:
          if (f =='2'): break
          else:
              print args
              print "OPENING FILE: "+f
              with open(f, "r") as src:
                write_class_meth_signat(src, to)
    print "BROKEN"
    for f in args:
        if (args[0] =='2'): break
        else: args.pop(0)
    print args
    if(args[0]=='2'):
        args.pop(0);
        print "2"
        print args
        if (args[0] =='no'):
          args.pop(0)
        else:
          print args
          print "OPENING FILE: "+f
          with open(f, "r") as src:
            write_output(src, to)
          args.pop(0)
    if(args[0]=='3'):
        args.pop(0);
        print "\n\nWRITING SOURCE\n\n"
        for f in args:
          print args
          print "OPENING FILE: "+f
          with open(f, "r") as src:
            write_source(src, to)
          args.pop(0)
    write_close(to)
  os.system("pdflatex -output-directory "+Dir+" "+ Dir+"main.tex")
  os.system("rm source.tex")
  


