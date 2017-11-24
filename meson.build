project('psautohint', 'c')

incdir = include_directories('libpsautohint/include')

lib_sources = [
    'libpsautohint/src/acfixed.c',
    'libpsautohint/src/ac.c',
    'libpsautohint/src/auto.c',
    'libpsautohint/src/bbox.c',
    'libpsautohint/src/charpathpriv.c',
    'libpsautohint/src/charprop.c',
    'libpsautohint/src/check.c',
    'libpsautohint/src/control.c',
    'libpsautohint/src/eval.c',
    'libpsautohint/src/fix.c',
    'libpsautohint/src/flat.c',
    'libpsautohint/src/fontinfo.c',
    'libpsautohint/src/gen.c',
    'libpsautohint/src/head.c',
    'libpsautohint/src/logging.c',
    'libpsautohint/src/memory.c',
    'libpsautohint/src/merge.c',
    'libpsautohint/src/misc.c',
    'libpsautohint/src/pick.c',
    'libpsautohint/src/psautohint.c',
    'libpsautohint/src/read.c',
    'libpsautohint/src/report.c',
    'libpsautohint/src/shuffle.c',
    'libpsautohint/src/stemreport.c',
    'libpsautohint/src/write.c',
]

cc = meson.get_compiler('c')
math = cc.find_library('m')

libpsautohint_so = shared_library(
    'psautohint',
    lib_sources,
    include_directories: incdir,
    dependencies: math,
)

libpsautohint_a = static_library(
    'psautohint',
    lib_sources,
    include_directories: incdir,
)

executable('autohintexe',
           'libpsautohint/autohintexe.c',
           link_with: libpsautohint_a,
           include_directories: incdir,
           dependencies: math)
