all: ve_Cnumba add_ints.so
	echo "Fist Wrapper"
	ve_Cnumba/bin/python python_wrapper.py
	echo
	echo "Second Wrapper"
	ve_Cnumba/bin/python python_wrapper_2.py

add_ints.so:
	gcc add_ints.c -fPIC -shared -o add_ints.so

ve_Cnumba:
	python3 -m venv ve_Cnumba
	ve_Cnumba/bin/pip install numpy numba ipython

clean:
	rm add_ints.so
	rm -rf ve_Cnumba