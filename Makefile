CV_YML = cv.yml
MARKDOWN_TEMPLATE = layouts/template.md
LATEX_TEMPLATE = layouts/template.tex

OUTDIR = _build
CV_MARKDOWN = $(OUTDIR)/cv.md
CV_LATEX = $(OUTDIR)/cv.tex
CV_PDF = $(OUTDIR)/cv.pdf

RENDER = ./render.py
LATEX_COMPILER = latexmk
PDF_VIEWER = xdg-open
LATEX_FLAGS = -pdf -outdir=$(OUTDIR)



all: $(CV_MARKDOWN) $(CV_LATEX)

show: $(CV_PDF)
	$(PDF_VIEWER) $<

clean:
	rm -rf $(OUTDIR)

$(CV_PDF): $(CV_LATEX)
	$(LATEX_COMPILER) $(LATEX_FLAGS) $<

$(CV_MARKDOWN): $(CV_YML) $(MARKDOWN_TEMPLATE) | $(OUTDIR)
	$(RENDER) --yml $< --template $(word 2,$^) --output $@

$(CV_LATEX): $(CV_YML) $(LATEX_TEMPLATE) | $(OUTDIR)
	$(RENDER) --yml $< --template $(word 2,$^) --output $@

$(OUTDIR):
	mkdir $(OUTDIR)
