.PHONY: all

ROOT_DIR = ..
SRC_DIR = $(ROOT_DIR)/source
PYT_DIR = $(ROOT_DIR)/python

FONTS:=$(wildcard data/*/*/font.ufo)
TESTS:=$(FONTS:%.ufo=%.tst)

all: $(TESTS)

%.tst: export PATH:=$(SRC_DIR):$(PATH)
%.tst: %.ufo $(SRC_DIR)/autohintexe $(PYT_DIR)/autohint.py
	@echo "	Testing $<"
	@rm -rf $@
	@python2 $(PYT_DIR)/autohint.py -all -q -o $@ $< 2>&1 >/dev/null