name=main
overhead=$(name).tex
pdfName=Report
tool=pdflatex
bib=bibtex
scripts=./rsc/scripts
bibFile=./Sections/references.bib
wordCount=$(scripts)/wordcount.py
wordNone=$(scripts)/singlewordcounter.py
replace=$(scripts)/replace.py
clean=$(scripts)/delatex.py
flatten=$(scripts)/flatten.py
syntax=$(scripts)/texcheck.py
noPic=$(scripts)/removePic.py
dict=./rsc/dict.txt
extension=odt

default: make

wordcount:
	@echo Checking the word count of the WORDCOUNT
	#@$(wordCount) Sections/simple.tex SECTION WORDCOUNT

avoidWord:
	@echo Checking for word you
	@$(wordNone) Sections/simple.tex "you"

extend:
	@echo Replacing isnt
	@for f in Sections/*.tex;do $(replace) $$f "isn't" "is not";done

endings:
	@echo Changing line endings for tex files
	@find ./ -name "*.tex" -type f -exec dos2unix {} +

spell: extend
	@echo Checking the spelling of the main tex file
	@echo $(overhead)
	@aspell -t -c --lang=en --dont-tex-check-comments $(overhead)
	@echo Checking the spelling within each Tex file
	@for f in Sections/*.tex;\
	do echo $$f; \
	aspell -t -c --lang=en --dont-tex-check-comments $$f ;\
	done
	@-mkdir tmp
	@-mv Sections/*.bak tmp

check: spell wordcount avoidWord endings

fix: clean check

build:	clean wordcount
	@echo Single Build
	@$(tool) $(overhead)
	@make syntax

flatten: $(overhead)
	@echo Flattening the document
	@$(flatten) $(overhead) total_$(name).tex

syntax: $(name).bbl
	@echo Removing the flattened file
	@-rm total_$(name).tex
	@echo Fixing the charset
	@sed -i 's/`/"/g' $(name).bbl
	@make flatten
	@echo Checking the syntax of the tex file
	@$(syntax) total_$(name).tex $(name).bbl
	@echo Removing the flattened file
	@-rm total_$(name).tex

fullBuild:	fix
	@echo Compiling the report
	@$(tool) $(overhead)
	@echo Building twice since the TOC is generated on second run
	@$(tool) $(overhead)
	@echo Running the bibliography
	@$(bib) $(name)
	@echo Recompiling the report with the bibliography
	@$(tool) $(overhead)
	@echo Building twice since the TOC is generated on second run
	@$(tool) $(overhead)
	@echo Renaming the report
	@mv $(name).pdf $(pdfName).pdf
	@echo Copying the outline to the README
	@make syntax

word:	fullBuild
	@-rm $(pdfName).$(extension)
	@make flatten
	@echo Removing the pictures
	@$(noPic) total_$(name).tex
	@echo Converting the latex file to Word Doc
	@pandoc total_$(name).tex --bibliography=$(bibFile) -o $(pdfName).$(extension)
	@make clean

make:	word

clean:
	@echo Removing the generated pictures
	@-rm Resources/UML/*.png
	@-rm Resources/UML/*.svg
	@-rm -r tmp/
	@-rmdir tmp/
	@-rm total_$(name).tex
	@-rm $(name).nlo
	@echo Cleaning the build directory
	@$(clean) ./
	@echo Cleaning backup files
	@find -type f -name "*.bak*" -exec rm -rf {} +
	@find -type f -name "*.log*" -exec rm -rf {} +

docClean: clean
	@echo Removing the compiled docs
	@- rm $(pdfName).pdf
	@- rm $(pdfName).$(extension)
