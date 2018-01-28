#!/usr/bin/env python3
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

SKOOL = 'sources/bts.skool'

SNAPSHOT = 'build/back_to_skool.z80'

OUTPUT = """Using skool file: sources/bts.skool
Using ref files: sources/bts.ref, sources/bugs.ref, sources/changelog.ref, sources/data.ref, sources/facts.ref, sources/glossary.ref, sources/graphics.ref, sources/pages.ref, sources/pokes.ref
Parsing sources/bts.skool
Creating directory {odir}/back_to_skool
Copying {SKOOLKIT_HOME}/skoolkit/resources/skoolkit.css to {odir}/back_to_skool/skoolkit.css
Copying sources/bts.css to {odir}/back_to_skool/bts.css
  Writing disassembly files in back_to_skool/asm
  Writing back_to_skool/maps/all.html
  Writing back_to_skool/maps/routines.html
  Writing back_to_skool/maps/data.html
  Writing back_to_skool/maps/messages.html
  Writing back_to_skool/buffers/gbuffer.html
  Writing back_to_skool/reference/bugs.html
  Writing back_to_skool/reference/changelog.html
  Writing back_to_skool/reference/facts.html
  Writing back_to_skool/reference/glossary.html
  Writing back_to_skool/graphics/glitches.html
  Writing back_to_skool/reference/pokes.html
  Writing back_to_skool/graphics/graphics.html
  Writing back_to_skool/graphics/playarea.html
  Copying sources/tiles.js to {odir}/back_to_skool/tiles.js
  Writing back_to_skool/graphics/patiles/patiles.html
  Writing back_to_skool/graphics/asstart.html
  Writing back_to_skool/graphics/as.html
  Writing back_to_skool/graphics/astiles/astiles.html
  Writing back_to_skool/buffers/cbuffer.html
  Writing back_to_skool/lessons/timetables.html
  Writing back_to_skool/lessons/index.html
  Writing back_to_skool/lessons/#N37.html
  Writing back_to_skool/lessons/#N38.html
  Writing back_to_skool/lessons/#N39.html
  Writing back_to_skool/lessons/#N40.html
  Writing back_to_skool/lessons/#N41.html
  Writing back_to_skool/lessons/#N42.html
  Writing back_to_skool/lessons/#N43.html
  Writing back_to_skool/lessons/#N44.html
  Writing back_to_skool/lessons/#N45.html
  Writing back_to_skool/lessons/#N46.html
  Writing back_to_skool/lessons/#N47.html
  Writing back_to_skool/lessons/#N48.html
  Writing back_to_skool/lessons/#N49.html
  Writing back_to_skool/lessons/#N50.html
  Writing back_to_skool/lessons/#N51.html
  Writing back_to_skool/lessons/#N52.html
  Writing back_to_skool/lessons/#N53.html
  Writing back_to_skool/lessons/#N54.html
  Writing back_to_skool/lessons/#N55.html
  Writing back_to_skool/lessons/#N56.html
  Writing back_to_skool/lessons/#N57.html
  Writing back_to_skool/lessons/#N58.html
  Writing back_to_skool/lessons/#N59.html
  Writing back_to_skool/tables/keys.html
  Parsing sources/load.skool
    Writing back_to_skool/load/load.html
    Writing disassembly files in back_to_skool/load
  Parsing sources/save.skool
    Writing back_to_skool/save/save.html
    Writing disassembly files in back_to_skool/save
  Parsing sources/start.skool
    Writing back_to_skool/start/start.html
    Writing disassembly files in back_to_skool/start
  Writing back_to_skool/index.html"""

HTML_WRITER = 'sources:backtoskool.BackToSkoolHtmlWriter'

ASM_WRITER = 'sources:backtoskool.BackToSkoolAsmWriter'

write_tests(SKOOL, SNAPSHOT, OUTPUT, HTML_WRITER, ASM_WRITER)
