#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

def write_tests(superclass_name, class_name, options_list, games):
    print('from btstest import {}'.format(superclass_name))
    print('')
    print('class {}({}):'.format(class_name, superclass_name))
    for game in games:
        for options in options_list:
            method_name_suffix = options.replace('-', '_').replace(' ', '')
            method_name = 'test_{}{}'.format(game, method_name_suffix)
            print("    def {}(self):".format(method_name))
            print("        self.write_{}('{}')".format(game, options))
            print("")

def get_asm_options_list():
    options_list = []
    for b in ('', '-D', '-H'):
        for c in ('', '-l', '-u'):
            for f in ('', '-f 1', '-f 2', '-f 3'):
                for p in ('', '-s', '-r'):
                    options_list.append('{} {} {} {}'.format(b, c, f, p).strip())
    return options_list

def get_ctl_options_list():
    options_list = []
    for w in ('', '-w b', '-w bt', '-w btd', '-w btdr', '-w btdrm', '-w btdrms', '-w btdrmsc'):
        for h in ('', '-h'):
            for a in ('', '-a'):
                for b in ('', '-b'):
                    options_list.append('{} {} {} {}'.format(w, h, a, b).strip())
    return options_list

def get_html_options_list():
    options_list = []
    for b in ('', '-D', '-H'):
        for c in ('', '-u', '-l'):
            options_list.append('{} {}'.format(b, c).strip())
    return options_list

TEST_TYPES = {
    'asm': get_asm_options_list(),
    'ctl': get_ctl_options_list(),
    'html': get_html_options_list(),
    'sft': ('', '-h', '-b', '-h -b')
}

###############################################################################
# Begin
###############################################################################
if not (len(sys.argv) == 2 and sys.argv[1] in TEST_TYPES):
    sys.stderr.write("Usage: {} asm|ctl|html|sft\n".format(os.path.basename(sys.argv[0])))
    sys.exit(1)
test_type = sys.argv[1]
superclass_name = '{}TestCase'.format(test_type.capitalize())
class_name = 'BackToSkool{}Test'.format(test_type.capitalize())
if test_type == 'asm':
    games = ['bts' + suffix for suffix in ('', '_load', '_save', '_start')]
else:
    games = ['bts']
write_tests(superclass_name, class_name, TEST_TYPES[test_type], games)
