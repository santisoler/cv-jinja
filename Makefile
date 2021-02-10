CV_YML = cv.yml
MARKDOWN_TEMPLATE = style/template.md
RENDER = ./render.py
OUTDIR = _build
CV_MARKDOWN = $(OUTDIR)/cv.md


all: $(CV_MARKDOWN)

clean:
	rm -rf $(OUTDIR)

$(CV_MARKDOWN): $(CV_YML) $(MARKDOWN_TEMPLATE) | $(OUTDIR)
	$(RENDER) --yml $< --template $(word 2,$^) --output $@

$(OUTDIR):
	mkdir $(OUTDIR)
