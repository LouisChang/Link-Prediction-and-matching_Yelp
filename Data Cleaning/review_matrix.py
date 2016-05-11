import json
import os
import time
import scipy as sp
#from decimal import Decimal

input_dir = "yelp_training_set_business.json"
output_dir = "output_user_review_count.txt"

graph = {}
hashtags_init = {}
output = []
name = []
user_id = []
star = []
business_id = []
state = []
with open(input_dir) as f:
    for ln in f: #read every tweet
        yelp = json.loads(ln)
        
        #user_id = yelp["user_id"]
        #star = yelp["stars"]
        #business_id=yelp["business_id"]
        state = yelp["state"]

        print state
        # Combine the data and ready to write file
        #output.append(review_count)
# Write the file
#with open(output_dir,'w') as out_f:
#    out_f.write(os.linesep.join(output))




