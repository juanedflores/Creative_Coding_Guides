# a wildcard that searches recursively
rwildcard = $(wildcard $1$2) $(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2))

# find all markdown files
MARKDOWN := $(call rwildcard,./,*.md)
PDF = $(MARKDOWN:.md=.pdf)

all: $(PDF)

%.pdf: %.md
	@echo $@
	pandoc /Users/juaneduardoflores/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/Zettelkasten/Game_Design/Game_Engines/Pico-8/00_getting_started.md -f markdown+implicit_figures+inline_code_attributes -o "/Users/juaneduardoflores/Documents/GitHub/Creative_Coding_Guides/PICO-8/00_getting_started.pdf" --template="/Users/juaneduardoflores/.pandoc/templates/eisvogel.tex" --pdf-engine="/Library/TeX/texbin/lualatex" --highlight-style="tango" --include-in-header="/Users/juaneduardoflores/.pandoc/headers/disable_float.tex" --lua-filter="/Users/juaneduardoflores/.pandoc/filters/columns.lua" --top-level-division="chapter" --filter="/Users/juaneduardoflores/Library/Python/3.9/bin/pandoc-latex-environment" -V colorlinks=true -V linkcolor=blue -V 'mainfont:AlgolRevived'


clean:
	rm $(PDF)
