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

SKOOL = 'bts.skool'

SNAPSHOT = 'build/back_to_skool.z80'

OUTPUT = """Using ref files: bts.ref, bugs.ref, changelog.ref, data.ref, facts.ref, glossary.ref, graphics.ref, pages.ref, pokes.ref, sound.ref
Parsing bts.skool
Output directory: {odir}/back_to_skool
Copying {SKOOLKIT_HOME}/skoolkit/resources/skoolkit.css to skoolkit.css
Copying bts.css to bts.css
Writing disassembly files in asm
Writing maps/all.html
Writing maps/routines.html
Writing maps/data.html
Writing maps/messages.html
Writing buffers/gbuffer.html
Writing reference/bugs.html
Writing reference/changelog.html
Writing reference/facts.html
Writing reference/glossary.html
Writing graphics/glitches.html
Writing reference/pokes.html
Writing graphics/graphics.html
Writing graphics/playarea.html
Copying tiles.js to tiles.js
Writing graphics/patiles.html
Writing graphics/asstart.html
Writing graphics/as.html
Writing graphics/astiles.html
Writing buffers/cbuffer.html
Writing lessons/timetables.html
Writing lessons/index.html
Writing lessons/#N37.html
Writing lessons/#N38.html
Writing lessons/#N39.html
Writing lessons/#N40.html
Writing lessons/#N41.html
Writing lessons/#N42.html
Writing lessons/#N43.html
Writing lessons/#N44.html
Writing lessons/#N45.html
Writing lessons/#N46.html
Writing lessons/#N47.html
Writing lessons/#N48.html
Writing lessons/#N49.html
Writing lessons/#N50.html
Writing lessons/#N51.html
Writing lessons/#N52.html
Writing lessons/#N53.html
Writing lessons/#N54.html
Writing lessons/#N55.html
Writing lessons/#N56.html
Writing lessons/#N57.html
Writing lessons/#N58.html
Writing lessons/#N59.html
Writing tables/keys.html
Writing sound/sound.html
Parsing load.skool
Writing load/load.html
Writing disassembly files in load
Parsing save.skool
Writing save/save.html
Writing disassembly files in save
Parsing start.skool
Writing start/start.html
Writing disassembly files in start
Writing index.html"""

write_tests(SKOOL, SNAPSHOT, OUTPUT)
