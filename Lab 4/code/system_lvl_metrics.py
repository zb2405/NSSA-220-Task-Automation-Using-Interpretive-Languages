import matplotlib.pyplot as plt
import numpy as np

def system_lvl_metrics() :
	time=[]
	rx=[]
	tx=[]
	writes=[]
	capacity=[]
	read_data("system_metrics.csv",time,rx,tx,writes,capacity)
		
	plot_2(time,rx,tx,"Data Rate (kB/sec)")
	plot_1(time,writes,"Disk Writes (kB/s)","Disk Writes")
	plot_1(time,capacity,"Disk Capacity (MB)","Disk Capacity")

def read_data (filename,s,r,t,w,c) :
	L =[]
	file = open(filename,"r")
	
	lines = file.readlines()

	for line in lines:

		L.append(line.strip().split(","))

	file.close()

	for data in L:
		s.append(int(data[0]))
		r.append(int(data[1]))
		t.append(int(data[2]))
		w.append(float(data[3]))
		c.append(int(data[4]))

def plot_1(x,y,y_label,l) :
	plt.plot(x,y,color = 'blue',label=l)
	plt.ylabel(y_label)
	plt.xlabel('Time (seconds)')
	plt.xlim(xmax = 900, xmin = 0)
	plt.legend(loc='lower center')

	if y_label == "Disk Writes (kB/s)":

		plt.title('Hard Disk Access Rates over Time')
		plt.ylim(ymax = 13000, ymin = 5000)
		plt.savefig('disk_access.png')
		plt.close()

	elif y_label == "Disk Capacity (MB)":

		plt.title('Hard Disk Utilization over Time')
		plt.ylim(ymax = 50000, ymin = 0)
		plt.savefig('disk_util.png')
		plt.close()	



def plot_2(x,y1,y2,y_label) :
	plt.plot(x,y1,color='blue',label='RX Data Rate')
	plt.plot(x,y2,color='red',label='TX Data Rate')
	plt.ylim(ymax = 100, ymin = 0)
	plt.xlim(xmax = 900, xmin = 0)
	plt.legend(loc='upper right')
	plt.ylabel(y_label)
	plt.xlabel('Time (seconds)')
	plt.title('Network Bandwidth Utilization over Time')
	plt.savefig('bandwidth.png')
	plt.close()	