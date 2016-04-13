# -*- coding: utf-8 -*-

import argparse

def load_user_keys(inputFile):
    user_dict = {}
    with open(inputFile) as fin:
        for line in fin:
            if line.find('# user_id') >= 0: continue
            line_contents = line.strip('\n').split('\t')
            user_id = int(line_contents[0])
            user_str_id = line_contents[1]
            user_dict[user_str_id] = user_id
    return user_dict        

def load_business_keys(inputFile):
    business_dict = {}
    with open(inputFile) as fin:
        for line in fin:
            if line.find('# business_id') >= 0: continue
            line_contents = line.strip('\n').split('\t')
            business_id = int(line_contents[0])
            business_str_id = line_contents[1]
            business_dict[business_str_id] = business_id
    return business_dict        

def checker(user_keys_file, business_keys_file, review_file, output_file):
    user_dict = load_user_keys(user_keys_file)
    business_dict = load_business_keys(business_keys_file)

    all_user = set(user_dict.keys())
    all_business = set(business_dict.keys())
    review_user_set = set()
    review_business_set = set()

    with open(review_file) as fin:
        for line in fin:
            if line.find('# user_id') >= 0: continue
            line_contents = line.strip('\n').split('\t')
            user_id = line_contents[0]
            business_id = line_contents[1]
            review_user_set.add(user_id)
            review_business_set.add(business_id)

    with open(output_file, 'w') as fout:
        fout.write('all_user = ' +  str(len(all_user)) + '\n')
        fout.write('all_business = ' +  str(len(all_business)) + '\n')
        fout.write('review_user = ' +  str(len(review_user_set)) + '\n')
        fout.write('review_business = ' +  str(len(review_business_set)) + '\n')
        fout.write('all_user - review_user = ' +  str(len(all_user - review_user_set)) + '\n')
        fout.write('all_business - review_business = ' +  str(len(all_business - review_business_set)) + '\n')

def main(args):
    user_keys_file = args.user_keys
    business_keys_file = args.business_keys
    review_file = args.review
    output_file = args.output
    checker(user_keys_file, business_keys_file, review_file, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process yelp tip data')
    parser.add_argument('--user_keys', metavar='FILE', required = True, 
                        help='user_keys file in tsv format')
    parser.add_argument('--business_keys', metavar='FILE', required = True, 
                        help='business_keys file in tsv format')
    parser.add_argument('--review', metavar='FILE', required = True, 
                        help='review file in tsv format')
    parser.add_argument('--output', metavar='FILE', required = True, 
                        help='output file')
    args = parser.parse_args()
    main(args)
