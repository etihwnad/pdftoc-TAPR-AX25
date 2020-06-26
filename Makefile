
SOURCE=AX25.2.2.pdf
INFO=toc.info
OUTPUT=AX25.2.2_toc.pdf


default: $(OUTPUT)


# mark the generated info file as transient
# this may need to change if the file is to include more than the ToC
.INTERMEDIATE: $(INFO)

$(SOURCE):
	wget http://www.tapr.org/pdf/AX25.2.2.pdf

$(INFO): toc.votl totoc.py
	./totoc.py $< > $@

$(OUTPUT): $(SOURCE) $(INFO)
	pdftk $(SOURCE) update_info $(INFO) output $(OUTPUT)


clean:
	rm -f $(INFO)
	rm -f $(OUTPUT)

clean-all: clean
	rm -f $(SOURCE)
