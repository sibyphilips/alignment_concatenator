#!/usr/bin/python

from Bio.Nexus import Nexus
# the combine function takes a list of tuples [(name, nexus instance)...],
#if we provide the file names in a list we can use a list comprehension to

# create these tuples with your filenames
#print "\n\n\nBe sure that you are working from the directory where the files are in!!!\n\n\n"
print("\n\n\nBe sure that you are working from the directory where the files are in!!!\n\n\n") #modified for python3

#lets add the files to a list so that the combine function can start working
file_list=[]
#a = raw_input("\nList out the NEXUS files that needs to be joined (separated by commas): ")
a = input("\nList out the NEXUS files that needs to be joined (separated by commas): ")
file_list = a.split(',')

print(file_list)
#file_list = ['atp6.nex',  'atp8.nex',  'atp9.nex',  'co1.nex',  'co2.nex',  'co3.nex',  'cytb.nex',  'nd1.nex',  'nd2.nex',  'nd3.nex',  'nd4l.nex',  'nd4.nex',  'nd5.nex',  'nd6.nex'
#]
nexi =  [(fname, Nexus.Nexus(fname)) for fname in file_list]

combined = Nexus.combine(nexi)
combined.write_nexus_data(filename=open('tuple.nex', 'w'))
