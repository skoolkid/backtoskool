#!/usr/bin/env python
import sys
import os

SKOOLKIT_HOME = os.environ.get('SKOOLKIT_HOME')
if not SKOOLKIT_HOME:
    sys.stderr.write('SKOOLKIT_HOME is not set; aborting\n')
    sys.exit(1)
if not os.path.isdir(SKOOLKIT_HOME):
    sys.stderr.write('SKOOLKIT_HOME={}: directory not found\n'.format(SKOOLKIT_HOME))
    sys.exit(1)
sys.path.insert(0, '{}/tools'.format(SKOOLKIT_HOME))
from testwriter import write_tests

SKOOL = '../sources/bts.skool'

SNAPSHOT = '../build/back_to_skool.z80'

OUTPUT = """Using skool file: ../sources/bts.skool
Using ref files: ../sources/bts.ref, ../sources/bts-bugs.ref, ../sources/bts-changelog.ref, ../sources/bts-data.ref, ../sources/bts-facts.ref, ../sources/bts-glossary.ref, ../sources/bts-graphics.ref, ../sources/bts-pages.ref, ../sources/bts-pokes.ref
Parsing ../sources/bts.skool
Creating directory {odir}/back_to_skool
Copying {SKOOLKIT_HOME}/skoolkit/resources/skoolkit.css to {odir}/back_to_skool/skoolkit.css
Copying ../sources/bts.css to {odir}/back_to_skool/bts.css
  Writing disassembly files in back_to_skool/asm
  Writing back_to_skool/maps/all.html
  Writing back_to_skool/maps/routines.html
  Writing back_to_skool/maps/data.html
  Writing back_to_skool/maps/messages.html
  Writing back_to_skool/buffers/gbuffer.html
  Writing back_to_skool/graphics/graphics.html
  Writing back_to_skool/graphics/playarea.html
  Copying ../sources/tiles.js to {odir}/back_to_skool/tiles.js
  Writing back_to_skool/graphics/patiles/patiles.html
  Writing back_to_skool/graphics/asstart.html
  Writing back_to_skool/graphics/as.html
  Writing back_to_skool/graphics/astiles/astiles.html
  Writing back_to_skool/buffers/cbuffer.html
  Writing back_to_skool/lessons/timetables.html
  Writing back_to_skool/lessons/index.html
  Writing back_to_skool/lessons/37.html
  Writing back_to_skool/lessons/38.html
  Writing back_to_skool/lessons/39.html
  Writing back_to_skool/lessons/40.html
  Writing back_to_skool/lessons/41.html
  Writing back_to_skool/lessons/42.html
  Writing back_to_skool/lessons/43.html
  Writing back_to_skool/lessons/44.html
  Writing back_to_skool/lessons/45.html
  Writing back_to_skool/lessons/46.html
  Writing back_to_skool/lessons/47.html
  Writing back_to_skool/lessons/48.html
  Writing back_to_skool/lessons/49.html
  Writing back_to_skool/lessons/50.html
  Writing back_to_skool/lessons/51.html
  Writing back_to_skool/lessons/52.html
  Writing back_to_skool/lessons/53.html
  Writing back_to_skool/lessons/54.html
  Writing back_to_skool/lessons/55.html
  Writing back_to_skool/lessons/56.html
  Writing back_to_skool/lessons/57.html
  Writing back_to_skool/lessons/58.html
  Writing back_to_skool/lessons/59.html
  Writing back_to_skool/tables/keys.html
  Writing back_to_skool/graphics/glitches.html
  Writing back_to_skool/reference/changelog.html
  Writing back_to_skool/reference/bugs.html
  Writing back_to_skool/reference/facts.html
  Writing back_to_skool/reference/glossary.html
  Writing back_to_skool/reference/pokes.html
  Parsing ../sources/load.skool
    Writing back_to_skool/load/load.html
    Writing disassembly files in back_to_skool/load
  Parsing ../sources/save.skool
    Writing back_to_skool/save/save.html
    Writing disassembly files in back_to_skool/save
  Parsing ../sources/start.skool
    Writing back_to_skool/start/start.html
    Writing disassembly files in back_to_skool/start
  Writing back_to_skool/index.html"""

HTML_WRITER = '../sources:backtoskool.BackToSkoolHtmlWriter'

ASM_WRITER = '../sources:backtoskool.BackToSkoolAsmWriter'

write_tests(SKOOL, SNAPSHOT, OUTPUT, HTML_WRITER, ASM_WRITER)
