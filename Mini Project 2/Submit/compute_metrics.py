def compute(ip,L,fname) :
	print('called compute function in compute_metrics.py')

	
	return(compute_metric(ip,L,fname))


def get_num(x):
	#This function grabs the numerical value from a string
	#returns a integer value of the grabbed number

    return int(''.join(num for num in x if num.isdigit()))

def compute_metric(ip,L,fname):
	reply_sent_count=0
	reply_rcvd_count=0
	request_sent_count=0
	request_rcvd_count=0
	bytes_sent=0
	bytes_rcvd=0
	data_sent=0
	data_rcvd=0
	count_1=0
	total_time_1=0
	count_2=0
	total_time_2=0
	avg_rtt=0
	avg_reply_delay=0
	request_throughput=0
	request_goodput=0
	org_hop=129
	hop_count=0
	request_count=0
	
	#index-
	#1: time
	#2:	Source IP
	#3:	Destination IP
	#5:	length
	#8: reply/request
	#11: ttl

	for item in L :
		if item[8] == "reply" :
			if item[2] == ip :
				reply_sent_count += 1 #Number of Echo Replies sent

		
			elif item[3] == ip :
				reply_rcvd_count += 1 #Number of Echo Replies received

		if item[8] == "request" :
			if item[2] == ip :
				request_sent_count += 1 #Number of Echo Requests sent
				bytes_sent += int(item[5]) #Total Echo Request bytes sent
				data_sent += int(item[5]) - 42 #Total Echo Request data sent (42 is the difference between ICMP packet size and ICMP payload size)

		
			elif item[3] == ip :
				request_rcvd_count += 1 #Number of Echo Requests received
				bytes_rcvd += int(item[5]) #Total Echo Request bytes received
				data_rcvd += int(item[5]) - 42 #Total Echo Request data received (42 is the difference between ICMP packet size and ICMP payload size)


	#calculation of required metrics for average round trip time, Echo Request Throughput, and Echo Request Goodput
	for i in range(0,len(L)):
		if L[i][8] == "request" :
			if L[i][2] == ip :
				count_1 += 1
				total_time_1 += (float(L[i+1][1]))-(float(L[i][1]))

	#calculation of required metrics for Average Reply Delay
	for i in range(0,len(L)):
		if L[i][8] == "request" :
			if L[i][3] == ip :
				count_2 += 1
				total_time_2 += (float(L[i+1][1]))-(float(L[i][1]))			
	
	#calculation of required metrics for Average Echo Request Hop Count
	for i in range(0,len(L)):
		if L[i][8] == "reply" :
			if L[i][3] == ip :
				hop_count += (org_hop - get_num(L[i][11]))
				

	
	avg_rtt = (total_time_1 / count_1)*1000 #Average Ping Round Trip Time
	request_throughput = (bytes_sent / total_time_1)/1000 #Echo Request Throughput (divide by thousand to convert ms to sec)
	request_goodput = (data_sent / total_time_1)/1000 #Echo Request Goodput
	avg_reply_delay = (total_time_2/count_2) * 1000000 #Average Reply Delay (multiply by 1000000 to get value in microseconds)
	avg_hop = float(hop_count)/float(request_sent_count) #Average Echo Request Hop Count

	
	# print(request_rcvd_count)
	# print(reply_sent_count)
	# print(reply_rcvd_count)
	# print(round(bytes_sent,2))
	# print(round(bytes_rcvd,2))
	# print(round(data_sent,2))
	# print(round(data_rcvd,2))
	# print(round(avg_rtt,2))
	# print(round(request_throughput,2))
	# print(round(request_goodput,2))
	# print(round(avg_reply_delay,2))
	# print(round(avg_hop,2))
	# print("\n")
	return(request_sent_count,request_rcvd_count,reply_sent_count,reply_rcvd_count,round(bytes_sent,2),round(data_sent,2),round(bytes_rcvd,2),round(data_rcvd,2),round(avg_rtt,2),\
		round(request_throughput,2),round(request_goodput,2),round(avg_reply_delay,2,),round(avg_hop,2))