# coding: utf-8

import glob
import os


def matched_exclude(fn, patterns):
    for pat in patterns.split(','):
        if glob.fnmatch.fnmatch(fn, pat.strip()):
            return True
    return False


def count_lines(directory, ext=None,
                exclude_patterns=None, exfuncs=None, detail=False):
    '''Count lines in each file inside directory

    ext: file extension to count
    exclude_patterns: comma separated patterns to ignore
    exfuncs: additional functions to exclude_patterns files from result
    '''
    if not exclude_patterns:
        exclude_patterns = '*.swp'
    if exfuncs is None:
        exfuncs = []

    if ext and not ext.startswith('.'):
        ext = '.' + ext
        exfuncs.append(lambda fn: not fn.endswith(ext))

    total_lines = 0
    for root, _, files in os.walk(directory):
        for f in files:
            c = 0

            path = os.path.join(root, f)
            if matched_exclude(path, exclude_patterns):
                continue

            if any(func(path) for func in exfuncs):
                continue

            try:
                with open(path) as fi:
                    for line in fi:
                        c += 1
            except UnicodeDecodeError as e:
                # pyc files, binary files...
                continue

            if detail:
                print("%7d: %s" % (c, path))

            total_lines += c
    return total_lines


def cli():
    import argparse
    argp = argparse.ArgumentParser()
    argp.add_argument('directory', default=['.'], nargs='*')
    argp.add_argument('-t', '--filetype', type=str, default='')
    argp.add_argument('-d', '--debug', action='store_true')
    argp.add_argument(
        '-e', '--exclude_patterns', type=str, default='',
        help='exclude_patterns: comma separated patterns to ignore'
    )

    args = argp.parse_args()
    ignore_git = [lambda f: '.git/' in f]
    for d in args.directory:
        total_lines = count_lines(d, args.filetype, args.exclude_patterns,
                                  detail=args.debug, exfuncs=ignore_git)
        print('%7d: %s' % (total_lines, d))
