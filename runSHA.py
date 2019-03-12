#!/usr/bin/env python3
import sys, os, argparse
import hashlib
import pandas as pd
import numpy as np

##############################################################################################################################################################
if __name__ == '__main__':
	""" Computes the sha256 hash for the main Darwin Core terms of a specimen
	"""
	# Read arguments
	parser = argparse.ArgumentParser("Insert the fulltext transcription for the text files in a folder.")
	parser.add_argument('-f', '--filename', action="store", required=True, help="Path and file name of the file to which sha256 will be applied")
	args = parser.parse_args()
	
    # Example: python3 ./runSHA.py -f ./idigbio/ec1ecd69-f213-433c-9df3-c7f149a7ab5b/occurrence.csv
    ##########################################################################################
	# The existence of the source file is verified
	if ( not os.path.isfile( args.filename ) ):
		print('Error: Input file does not exist or is not reachable.\n')
		parser.print_help()
		sys.exit(1)

	df = pd.read_csv(args.filename, sep=',')
	df = df.replace(np.nan, '')
	i = 0
	for index, row in df.iterrows():
		s = row["dwc:country"] + row["dwc:eventDate"] + row["dwc:scientificName"] + row["dwc:recordedBy"] + row["dwc:verbatimLocality"]
		hash_object = hashlib.sha256( s.encode('utf-8') )
		hex_dig = hash_object.hexdigest()
		print(hex_dig)
		i = i + 1
		if i == 20:
			break

	# print(df[["dwc:country"]])
	# print(df[["dwc:eventDate"]])
	# print(df[["dwc:scientificName"]])
	# print(df[["dwc:recordedBy"]])
	# print(df[["dwc:verbatimLocality"]])

	#df.where(pd.notnull(df), None)
	#hash_object = hashlib.sha256(b'Hello World')
	#hex_dig = hash_object.hexdigest()
	#print(hex_dig)
