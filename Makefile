##
# Copyright 2012 Yummy Melon Software LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Charles Y. Choi


PYTHONPATH=${PWD}

exampleDiagrams:
	cd examples; PYTHONPATH=${PYTHONPATH} python authentication.py
	cd examples; PYTHONPATH=${PYTHONPATH} python nestedActivation.py
	cd examples; PYTHONPATH=${PYTHONPATH} python concurrentProcessesActivations.py
	cd examples; PYTHONPATH=${PYTHONPATH} python createDestroy.py
	cd examples; PYTHONPATH=${PYTHONPATH} python lifelineConstraints.py
	cd examples; PYTHONPATH=${PYTHONPATH} python externalActor.py
	cd examples; PYTHONPATH=${PYTHONPATH} python comment.py

regression:
	cd tests; PYTHONPATH=${PYTHONPATH} python -m unittest test_SequenceDiagram.TestSequenceDiagram

docs:
	make -C doc


clean:
	cd sequenceplot; rm -f *~ *.pyc
	cd examples; rm -f *.pic *.svg *~
	cd doc; rm -f *.html


