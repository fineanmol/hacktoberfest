#!/usr/bin/env python
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='output file name')
    parser.add_argument('files', nargs='+')
    args=parser.parse_args()
    cmd = 'gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dAutoRotatePages=/None -sOutputFile={} {}'.format(args.output, ' '.join(args.files))
    print(cmd)
    os.system(cmd)
    print('output file {}'.format(args.output))
