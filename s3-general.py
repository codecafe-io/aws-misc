#!/usr/bin/env python
import boto
import os.path
import sys
import os
import glob
from boto.s3.key import Key
import boto

'''
Syntax for the functions are is program name and the command
ex: s3.options.py <command>
'''

action = str(sys.argv[1])
bucket_name = str(sys.argv[2])

s3=boto.connect_s3()

# Create a bucket if the bucket does not exist

if action == "create-bucket":
    if not s3.lookup(bucket_name):
        print ("creating bucket")
        s3.create_bucket(bucket_name)

# Create a new key and value inside s3 (object)
# key.key is the name of the file
# key.set_content... is the content of that file
if action == "create-object":
    bucket = s3.get_bucket(bucket_name)
    key = Key(bucket)
    key.key = sys.argv[3]
    key.set_contents_from_strings(sys,argv[4])
    
if action == "upload-text-files":
    bucket = s3.get_bucket(bucket_name)
    print "upload all txt files to " + bucket_name
    for filename in glob.glob("*.txt"):
        key = bucket.new_key("files/"+ filename)
        key.set_contents_from_filename(filename)
        print "uploaded files" + filename
    
if action == "delete-bucket"):
    bucket = s3.get_bucket(bucket_name)
    for key in bucket.list():
        key.delete()
    s3.delete_bucket(bucket_name)

if action ="create-website":
    bucket=s3.create_bucket(bucket_name)
    index_file = bucket.new_key('index.html')
    index_file.content_type = "text/html"
    error_file = bucket.new_key('error.html')
    error_file.content_type = "text/html"

    index_html = "<html> <head> <title> Coming Soon </title></head><body><h1> Coming Soon </h1></body></html>"
    error_html = "<html> <head> <title> Error </title></head><body><h1> Error </h1></body></html>"
    index_file.set_contents_from_string(index_html, policy='public-read')
    error_file.set_contents_from_string(error_html, policy='public-read')
    
    bucket.configure_website('index.html','error_html')

    print "website url "+ bucket.get_website_endpoint