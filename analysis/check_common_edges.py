# -*- coding: utf-8 -*-

import argparse
import os

""" check overlap of (user, review) pairs in train and test data sets """

def checker(inputFile):
    S = set()
    with open(inputFile) as fin:
        for line in fin:
            if line.find('# user_id') >= 0: continue
            if line.find('# business_id') >= 0: continue
            line_contents = line.strip('\n').split('\t')
            user_id = line_contents[0]
            business_id = line_contents[1]
            e = (user_id, business_id)
            S.add(e)
    return S

def main(args):
    train_data_file = args.train_data
    test_data_file = args.test_data
    issimple = args.simple

    shortname_train = os.path.basename(train_data_file)
    shortname_test = os.path.basename(test_data_file)
    Train = checker(train_data_file)
    Test = checker(test_data_file)
    Common = Train & Test
    
    if issimple == 0:   
        print "(user, business) edges: "
        print "\t%s: %d" % (shortname_train, len(Train))
        print "\t%s: %d" % (shortname_test, len(Test))
        print "\t%s: %d" % ('common', len(Common))
    else:
        print "%d" % len(Common)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process yelp tip data')
    parser.add_argument('--train_data', metavar='FILE', required = True, help='train data')
    parser.add_argument('--test_data', metavar='FILE', required = True, help='test data')
    parser.add_argument('--simple', type=int, required = False, default=0, help='test data')
    args = parser.parse_args()
    main(args)
