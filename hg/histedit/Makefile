PYTHON=python

help:
	@echo 'Commonly used make targets:'
	@echo '  tests              - run all tests in the automatic test suite'
	@echo '  all-version-tests - run all tests against many hg versions'
	@echo '  tests-%s           - run all tests in the specified hg version'

all: help

tests:
	cd tests && $(PYTHON) $(CREW)/tests/run-tests.py $(TESTFLAGS)

test-%:
	cd tests && $(PYTHON) $(CREW)/tests/run-tests.py $(TESTFLAGS) $@

tests-%:
	@echo "Path to crew repo is $(CREW) - set this with CREW= if needed."
	hg -R $(CREW) checkout $$(echo $@ | sed s/tests-//) && \
	(cd $(CREW) ; $(MAKE) clean ) && \
	cd tests && $(PYTHON) $(CREW)/tests/run-tests.py $(TESTFLAGS)

all-version-tests: tests-1.4.3 tests-1.5.4 \
                   tests-1.6.4 tests-1.7.5 tests-1.8.3 tests-1.9.3 tests-2.0 \
                   tests-tip

.PHONY: tests all-version-tests
