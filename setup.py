import platform
from setuptools import setup, Extension


module1 = Extension("psautohint._psautohint",
                    include_dirs=[
                        "source/include",
                    ],
                    sources=[
                        "python/psautohint/_psautohint.c",
                        "source/ac/ac.c",
                        "source/ac/ac_C_lib.c",
                        "source/ac/acfixed.c",
                        "source/ac/auto.c",
                        "source/ac/bbox.c",
                        "source/ac/charpath.c",
                        "source/ac/charprop.c",
                        "source/ac/check.c",
                        "source/ac/control.c",
                        "source/ac/eval.c",
                        "source/ac/fix.c",
                        "source/ac/flat.c",
                        "source/ac/fontinfo.c",
                        "source/ac/gen.c",
                        "source/ac/head.c",
                        "source/ac/logging.c",
                        "source/ac/memory.c",
                        "source/ac/merge.c",
                        "source/ac/misc.c",
                        "source/ac/pick.c",
                        "source/ac/read.c",
                        "source/ac/report.c",
                        "source/ac/shuffle.c",
                        "source/ac/stemreport.c",
                        "source/ac/write.c",
                    ]
        )

setup(name="psautohint",
      version="1.1.0.dev0",
      description="Python wrapper for Adobe's PostScript autohinter",
      url='https://github.com/khaledhosny/psautohint',
      author='Khaled Hosny',
      author_email='khaledhosny@eglug.org',
      license='Apache License, Version 2.0',
      package_dir={'': 'python'},
      packages=['psautohint'],
      ext_modules=[module1],
      entry_points={
          'console_scripts': [
              "autohint = psautohint.autohint:main",
          ],
      },
      install_requires=[
          'fonttools>=3.1.2',
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Text Processing :: Fonts',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Multimedia :: Graphics :: Graphics Conversion',
      ],
    )
