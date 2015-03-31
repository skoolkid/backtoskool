import sys
import os

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
skool2html_options = '-d {0}/build/html -S {0}/resources'.format(PARENT_DIR)

SKOOLKIT_HOME = os.environ.get('SKOOLKIT_HOME')
if SKOOLKIT_HOME:
    if not os.path.isdir(SKOOLKIT_HOME):
        sys.stderr.write('SKOOLKIT_HOME={}: directory not found\n'.format(SKOOLKIT_HOME))
        sys.exit(1)
    sys.path.insert(0, SKOOLKIT_HOME)
    from skoolkit import skool2asm, skool2html
    skool2html_options += ' -S {}/resources'.format(SKOOLKIT_HOME)
else:
    try:
        from skoolkit import skool2asm, skool2html
    except ImportError:
        sys.stderr.write('Error: SKOOLKIT_HOME is not set, and SkoolKit is not installed\n')
        sys.exit(1)

sys.stderr.write("Found SkoolKit in {}\n".format(skool2html.PACKAGE_DIR))

def run_skool2asm(writer, skoolfile):
    writer_class = '{}/skoolkit:{}'.format(PARENT_DIR, writer)
    options = '-W {}'.format(writer_class)
    args = options.split() + sys.argv[1:] + ['{}/{}'.format(PARENT_DIR, skoolfile)]
    skool2asm.main(args)

def run_skool2html(writer, reffile):
    writer_class = '{}/skoolkit:{}'.format(PARENT_DIR, writer)
    options = '-W {} {}'.format(writer_class, skool2html_options)
    args = options.split() + sys.argv[1:] + ['{}/{}'.format(PARENT_DIR, reffile)]
    skool2html.main(args)
