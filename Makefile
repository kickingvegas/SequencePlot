##
# Copyright 2012 Yummy Melon Software LLC
# Author: Charles Y. Choi
#

PYTHONPATH=${PWD}
docs:
	make -C doc


clean:
	cd sequenceplot; rm -f *~ *.pyc
	cd examples; rm -f *.pic *.svg
	cd doc; rm -f *.html


