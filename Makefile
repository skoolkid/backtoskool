SNAPSHOT = $(shell grep -Po 'SNAPSHOT=\$$BACKTOSKOOL_HOME/\K.*' .ddiffsrc)
T2S = back_to_skool.t2s

MK = $(SKOOLKIT_HOME)/tools/disassembly.mk
ifeq ($(wildcard $(MK)),)
    $(error $(MK): file not found)
endif
include $(MK)
