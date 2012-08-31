#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os
import sys
try:
    import acoustid
except:
    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(PROJECT_DIR)
    import acoustid

def main(argv):
    def exit_with_usage():
        print 'usage: $ python',__file__,'/path/to/foo.mp3'
    if len(argv) != 2:
        return exit_with_usage()
    else:
        path = argv[1]
    dur, fp_raw = acoustid.fingerprint_file(path,return_raw=True)
    dur, fp_str = acoustid.fingerprint_file(path)
    print 'duration:',dur
    print 'fingerprint str:',fp_str
    print 'fingerprint raw:',fp_raw

if __name__ == '__main__':
    main(sys.argv)
