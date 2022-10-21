#!/usr/bin/env python3

from person import Person
from numba import njit
import matplotlib.pyplot as plt
from time import perf_counter as pc

def fib_py(n):
	if n<=1:
		return 1
	else:
		return fib_py(n-1)+fib_py(n-2)

@njit
def fib_numba(n):
	if n<=1:
		return 1
	else:
		return fib_numba(n-1)+fib_numba(n-2)


def plot20_30():
# Plot for 20-30
	n_py = []
	time_py = []
	i=1
	for i in range (11):
		i+=20
		start = pc()
		fib_py(i)
		end = pc()
		time_py.append(end-start)
		n_py.append(i)

	n_numba = []
	time_numba = []
	i=1
	for i in range (11):
		i+=20
		start = pc()
		fib_numba(i)
		end = pc()
		time_numba.append(end-start)
		n_numba.append(i)

	plt.scatter(n_py, time_py, c="blue", label="fib_py(n)")
	plt.scatter(n_numba, time_numba, c="red", label = "fib_numba(n)")
	plt.xlabel("n")
	plt.legend()
	plt.ylabel("time in seconds")
	print("successful")
#	plt.savefig("Fib_20-30_time_plot_final.png", dpi=300)


def plot30_45():
# Plot for 30-45
	n_py = []
	time_py = []
	i=1
	for i in range(16):
		i+=30
		start = pc()
		fib_py(i)
		end = pc()
		time_py.append(end-start)
		n_py.append(i)

	n_numba = []
	time_numba = []
	i=1
	for i in range(16):
		i+=30
		start = pc()
		fib_numba(i)
		end = pc()
		time_numba.append(end-start)
		n_numba.append(i)

	n_cpp = []
	time_cpp = []
	i = 1
	for i in range(16):
		i+=30
		f=Person(i)
		start = pc()
		f.fib()
		end = pc()
		time_cpp.append(end-start)
		n_cpp.append(i)

	plt.scatter(n_py, time_py, c = "blue", label="fib_py(n)")
	plt.scatter(n_numba, time_numba, c = "red", label = "fib_numba(n)")
	plt.scatter(n_cpp, time_cpp, c = "green", label = "f=Person(n);f.fib()")
	plt.title("Time to calculate Fibonacci of n")
	plt.xlabel("n")
	plt.legend()
	plt.ylabel("time in seconds")
#	plt.savefig("Fib_30-45_time_plot_final.png", dpi=300)


def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(f.fib())
	#plot20_30()
	#plot30_45()
	print(fib_numba(47))
	f=Person(47)
	print(f.fib())

if __name__ == '__main__':
	main()
	
