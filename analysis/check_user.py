# -*- coding: utf-8 -*-

import argparse
import simplejson as json

def check_user_key(inputFile):
    users = set()
    all_users = set()
    with open(inputFile) as fin:
        for line in fin:
            line_contents = json.loads(line)
            user_id = line_contents['user_id']
            friends = line_contents['friends']
            users.add(user_id)
            all_users.add(user_id)
            for f in friends:
                all_users.add(f)
    unknown_users = all_users - users
    print "all_users+friends = ",len(all_users)
    print "all_users = ",len(users)
    print "unknown_users = ", len(unknown_users)

def main(args):
    inputFile = args.input
    check_user_key(inputFile)   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process yelp tip data')
    parser.add_argument('--input', metavar='FILE', required = True,
                        help='input file in json format')
    args = parser.parse_args()
    main(args)
