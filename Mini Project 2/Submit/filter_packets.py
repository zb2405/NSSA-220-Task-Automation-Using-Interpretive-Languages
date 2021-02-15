def read_write(filename, num):
    filteredfile = "Node" + str(num) + "_filtered.txt"
    f = open(filename, "r")
    file = open(filteredfile, "w")
    lines = f.readlines()

    for line in lines:
        if 'ping' in line:
            file.write(line)
    f.close()
    file.close()    

def filter():
    read_write("Node1.txt",1)
    read_write("Node2.txt",2)
    read_write("Node3.txt",3)
    read_write("Node4.txt",4)
