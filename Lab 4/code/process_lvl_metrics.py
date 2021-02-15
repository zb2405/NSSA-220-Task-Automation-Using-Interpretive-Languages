import matplotlib.pyplot as plt
import numpy as np


def process_lvl_metrics():
	time_apm=[]
	apm1 = []
	cpu_apm1 = []
	mem_apm1 = []
	read_data("APM1_metrics.csv",apm1,cpu_apm1,mem_apm1)
	
	for data in apm1:
		time_apm.append(int(data[0]))

	
	apm2 = []
	cpu_apm2 = []
	mem_apm2 = []
	read_data("APM2_metrics.csv",apm2,cpu_apm2,mem_apm2)
	

	apm3 = []
	cpu_apm3 = []
	mem_apm3 = []
	read_data("APM3_metrics.csv",apm3,cpu_apm3,mem_apm3)

	cpu_apm4 = []
	mem_apm4 = []
	apm4 = []
	read_data("APM4_metrics.csv",apm4,cpu_apm4,mem_apm4)

	cpu_apm5 = []
	mem_apm5 = []
	apm5 = []
	read_data("APM5_metrics.csv",apm5,cpu_apm5,mem_apm5)

	apm6 = []
	cpu_apm6 = []
	mem_apm6 = []
	read_data("APM6_metrics.csv",apm6,cpu_apm6,mem_apm6)

	plot(time_apm,cpu_apm1,cpu_apm2,cpu_apm3,cpu_apm4,cpu_apm5,cpu_apm6,"CPU(%)")
	plot(time_apm,mem_apm1,mem_apm2,mem_apm3,mem_apm4,mem_apm5,mem_apm6,"MEM(%)")




def read_data(filename, L,cpu,mem):
	file = open(filename,"r")
	
	lines = file.readlines()


	for line in lines:

		L.append(line.strip().split(","))

	file.close()
	
	for data in L:
		cpu.append(float(data[1]))
		mem.append(float(data[2]))

def plot(x,y1,y2,y3,y4,y5,y6,y_label):
	plt.plot(x,y1,color='blue',label='APM1')
	plt.plot(x,y2,color='black',label='APM2')
	plt.plot(x,y3,color='red',label='APM3')
	plt.plot(x,y4,color='green',label='APM4')
	plt.plot(x,y5,color='yellow',label='APM5')
	plt.plot(x,y6,color='cyan',label='APM6')
	plt.ylim(ymax = 100, ymin = -1)
	plt.xlim(xmax = 900, xmin = 0)
	plt.legend(loc='upper right')
	plt.ylabel(y_label)
	plt.xlabel('Time (seconds)')

	if y_label == "CPU(%)":
		plt.title('CPU Utilization over time')
		plt.savefig('cpu.png')
		plt.close()
	elif y_label == "MEM(%)":

		plt.title('Memory Utilization over time')
		plt.savefig('memory.png')
		plt.close()	

