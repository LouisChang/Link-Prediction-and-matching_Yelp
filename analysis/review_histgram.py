# -*- coding: utf-8 -*-

import argparse
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

USER_MAX_BIN = 10 + 1
USER_HIST_BINS = range(USER_MAX_BIN+1)

BUSINESS_MAX_BIN = 50 + 1
BUSINESS_HIST_BINS = range(BUSINESS_MAX_BIN+1)

def process(review_file, output_hist_user_file, output_hist_business_file):
    groupby_user = defaultdict(list)
    groupby_business = defaultdict(list)
    with open(review_file) as fin:
        for line in fin:
            if line.find('# user_id') >= 0: continue
            line_contents = line.strip('\n').split('\t')
            uid = line_contents[0]
            bid = line_contents[1]
            groupby_user[uid].append(bid)
            groupby_business[bid].append(uid)

    # user data          
    UserDict = defaultdict(int)
    for uid in groupby_user:
        UserDict[uid] = len(groupby_user[uid])
    A = list(UserDict.values())
    B = np.clip(A, 0, USER_MAX_BIN)
    hist, bin_edges = np.histogram(B, bins=USER_HIST_BINS)
    # np.savetxt(output_hist_user_file+'.tsv', hist, fmt='%d', delimiter='\t')
    myplot(
           bin_edges, 
           hist, 
           'Number of Reviews', 
           'Number of Users', 
           'User Review Histogram',
            output_hist_user_file)
    
        
    # biz data          
    BizDict = defaultdict(int)
    for bid in groupby_business:
        BizDict[bid] = len(groupby_business[bid])
        
    A = list(BizDict.values())
    B = np.clip(A, 0, BUSINESS_MAX_BIN)
    hist, bin_edges = np.histogram(B, bins=BUSINESS_HIST_BINS)
    # np.savetxt(output_hist_business_file+'.tsv', hist, fmt='%d',delimiter='\t')
    myplot(
           bin_edges, 
           hist, 
           'Number of Reviews', 
           'Number of Business', 
           'Business Review Histogram',
            output_hist_business_file)

def myplot(bin_edges, hist, xlbl, ylbl, title, outfile):
    plt.figure()
    plt.clf()
    pp = PdfPages(outfile+'.pdf')
    plt.bar(bin_edges[:-1], hist, width = 0.75)
    plt.grid()
    plt.title(title, fontsize=20)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    pp.savefig()
    pp.close()
    
def main(args):
    review_file = args.review
    output_hist_user_file = args.output_hist_user
    output_hist_business_file = args.output_hist_business
    process(review_file, output_hist_user_file, output_hist_business_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process yelp tip data')
    parser.add_argument('--review', metavar='FILE', required = True, 
                        help='review file in tsv format')
    parser.add_argument('--output_hist_user', metavar='FILE', required = True, 
                        help='output_hist_user file')
    parser.add_argument('--output_hist_business', metavar='FILE', required = True, 
                        help='output_hist_business file')
    args = parser.parse_args()
    main(args)
