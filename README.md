Back to Skool disassembly
=========================

A disassembly of the [Spectrum](https://en.wikipedia.org/wiki/ZX_Spectrum) game
[Back to Skool](https://en.wikipedia.org/wiki/Back_to_Skool), created using
[SkoolKit](https://skoolkit.ca).

Decide which number base you prefer and then click the corresponding link below
to browse the latest release:

* [Back to Skool disassembly](https://skoolkid.github.io/backtoskool/) (hexadecimal; mirror [here](https://skoolkid.gitlab.io/backtoskool/))
* [Back to Skool disassembly](https://skoolkid.github.io/backtoskool/dec/) (decimal; mirror [here](https://skoolkid.gitlab.io/backtoskool/dec/))

To build the current development version of the disassembly, first obtain the
development version of [SkoolKit](https://github.com/skoolkid/skoolkit). Then:

    $ skool2html.py sources/bts.skool

To build an assembly language source file that can be fed to an assembler:

    $ skool2asm.py sources/bts.skool > bts.asm
