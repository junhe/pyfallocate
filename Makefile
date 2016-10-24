all: pyfallocate/_fallocate.so

test:
	python -m unittest discover -s tests -p '*test*.py'

pyfallocate/_fallocate.so: pyfallocate/fallocate_build.py
	python $<

clean:
	rm pyfallocate/_*.c pyfallocate/_*.o pyfallocate/_*.so
