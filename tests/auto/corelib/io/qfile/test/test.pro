CONFIG += testcase
QT = core-private core testlib
qtHaveModule(network): QT += network
else: DEFINES += QT_NO_NETWORK

contains(CONFIG, builtin_testdata) {
    DEFINES += BUILTIN_TESTDATA
}

TESTDATA += ../BLACKLIST

debug_and_release {
    CONFIG(debug, debug|release) {
        TARGET = ../../debug/tst_qfile
    } else {
        TARGET = ../../release/tst_qfile
    }
} else {
    TARGET = ../tst_qfile
}
SOURCES = ../tst_qfile.cpp
INCLUDEPATH += ../../../../../shared/
HEADERS += ../../../../../shared/emulationdetector.h

RESOURCES += ../qfile.qrc ../rename-fallback.qrc ../copy-fallback.qrc

TESTDATA += ../dosfile.txt ../noendofline.txt ../testfile.txt \
            ../testlog.txt ../two.dots.file ../tst_qfile.cpp \
            ../Makefile ../forCopying.txt ../forRenaming.txt \
            ../resources/file1.ext1

win32:!winrt: LIBS+=-lole32 -luuid
