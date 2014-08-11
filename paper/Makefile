all:
	pdflatex paper

up: 
	svn16 up
	
commit:
	svn16 commit -m "diego - minor"
	

minor: up
	svn16 commit -m "diego - minor"
	

clean: 
	rm -f *toc *ps *log *idx *~ *conflicted* *aux *bbl
	rm -f *ilg *blg *save *ind *dvi *bak Icon* Temp.tex
	rm -f *{maf,mtc,mtc0,out}
	rm -f images/*log
	
	
