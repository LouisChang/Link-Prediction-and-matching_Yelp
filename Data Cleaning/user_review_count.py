import json
import os
import time
import scipy as sp
#from decimal import Decimal

input_dir = "yelp_training_set_user.json"
output_dir = "output_user_review_count.txt"

graph = {}
hashtags_init = {}
output = []
name = []
review_count = []
user_review_count = []

with open(input_dir) as f:
    for ln in f: #read every tweet
        yelp = json.loads(ln)
        
        name = yelp["user_id"]
        user_review_count = yelp["review_count"]
        
        print user_review_count
        # Combine the data and ready to write file
        #output.append(review_count)
# Write the file
#with open(output_dir,'w') as out_f:
#    out_f.write(os.linesep.join(output))




