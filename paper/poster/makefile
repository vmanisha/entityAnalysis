BASEFILENAME=poster

all:
	make clean
	make pdf

dvi:
	latex ${BASEFILENAME}.tex
	#bibtex ${BASEFILENAME}
	latex ${BASEFILENAME}.tex
	latex ${BASEFILENAME}.tex
	
ps:
	make dvi
	dvips ${BASEFILENAME}.dvi

pdf:
	make dvi
	dvipdf ${BASEFILENAME}.dvi
	open ${BASEFILENAME}.pdf

count:
	pdftotext ${BASEFILENAME}.pdf
	wc --words ${BASEFILENAME}.txt

clean:
	rm -f fig/*~ *~ *aux *dvi *log *out *pdf *bbl *blg *ps *idx *toc *txt *fdb_latexmk *.synctex.gz

edit:
	open -a textmate ${BASEFILENAME}.tmproj

zip:
	tar -czf $(PWD)\ `date +%Y%m%d%H%M`.tgz *tex *bib fig/*

commit:
	svn update
	svn commit -m `date +%Y%m%d%H%M`-FM

update:
	svn update

