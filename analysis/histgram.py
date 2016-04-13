# -*- coding: utf-8 -*-

import argparse
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

USER_MAX_BIN = 20 + 1
USER_HIST_BINS = range(USER_MAX_BIN+1)

BUSINESS_MAX_BIN = 20 + 1
BUSINESS_HIST_BINS = range(BUSINESS_MAX_BIN+1)

def process(review_file, user_hist_file, business_hist_file):
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
    np.savetxt(user_hist_file+'.tsv', hist, fmt='%d', delimiter='\t')
    myplot(
           bin_edges, 
           hist, 
           'Number of Reviews', 
           'Number of Users', 
           'User Review Histogram',
            user_hist_file)
    
        
    # biz data          
    BizDict = defaultdict(int)
    for bid in groupby_business:
        BizDict[bid] = len(groupby_business[bid])
        
    A = list(BizDict.values())
    B = np.clip(A, 0, BUSINESS_MAX_BIN)
    hist, bin_edges = np.histogram(B, bins=BUSINESS_HIST_BINS)
    np.savetxt(business_hist_file+'.tsv', hist, fmt='%d',delimiter='\t')
    myplot(
           bin_edges, 
           hist, 
           'Number of Reviews', 
           'Number of Business', 
           'Business Review Histogram',
            business_hist_file)

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
    user_hist_file = args.user_hist
    business_hist_file = args.business_hist
    process(review_file, user_hist_file, business_hist_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process yelp tip data')
    parser.add_argument('--review', metavar='FILE', required = True, 
                        help='review file in tsv format')
    parser.add_argument('--user_hist', metavar='FILE', required = True, 
                        help='user_hist file')
    parser.add_argument('--business_hist', metavar='FILE', required = True, 
                        help='business_hist file')
    args = parser.parse_args()
    main(args)