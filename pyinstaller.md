## PyInstaller Notes

### FileGDB

Include additional dlls required by FileGDB

Add the following in the .spec file

```
a.binaries += [('msvcp100.dll', 'C:\\Windows\\System32\\msvcp100.dll', 'BINARY'),
               ('msvcr100.dll', 'C:\\Windows\\System32\\msvcr100.dll', 'BINARY')]
```

### Pandas

Workaround for [PyInstaller bug #1580 pandas: C extension pandas.lib not included](https://github.com/pyinstaller/pyinstaller/issues/1580)

Add the following in the .spec file

```
a.binaries += [('pandas.lib.pyd', 'release-env\Lib\site-packages\pandas\lib.pyd', 'BINARY')]
```

### Debugging exe

Using debug option in the spec

In the spec file:

```
exe = EXE(pyz,
  a.scripts,# + [('v', '', 'OPTION')],
  exclude_binaries=True,
  name='myapp.exe',
  #debug=False,
  debug=True,
  strip=None,
  upx=True,
  #console=False,
  console=True,
)
```

### Known Issues

#### (1)  Error: LOADER: RC: -1 from pyi_rth_pkgres

If you see the following PyInstaller error with the debug mode enabled in the spec file

```
 Traceback (most recent call last):                                                                                                                                                         
      File "<string>", line 11, in <module>                                                                                                                                                    
      File "c:\users\username\appdata\local\temp\pip-build-qovult\PyInstaller\PyInstaller\loader\pyi_importers.py", line 270, in load_module                                                      
      File "C:\build\endeavour\out00-PYZ.pyz\pkg_resources", line 75, in <module>                                                                                 
      File "C:\build\endeavour\out00-PYZ.pyz\pkg_resources.extern", line 60, in load_module                                                                       
    ImportError: The 'packaging' package is required; normally this is bundled with this package so if you get this warning, consult the packager of your distribution.                        
    LOADER: RC: -1 from pyi_rth_pkgres
```

Solution: 

The issue is caused by latest version of setuptools. Downgrading setuptools from 20.2.2 to 19.2 solves the problem ([ext-link](https://github.com/pyinstaller/pyinstaller/issues/1781)). 


#### (2)  Error: LOADER: RC: -1 from main (ImportError: No module named tz)

If you see the following PyInstaller error with the debug mode enabled in the spec file


```
ImportError: No module named tz
LOADER: RC: -1 from main
```

Solution:

The issue is caused by latest version of python-dateutil. Downgrading python-dateutil from 2.5.0 to 2.4.2 solves the problem.


#### (3) Error: checkCache os.remove(cachedfile) WindowsError: [Error 2] The system cannot find the file specified

If you see the following error (related to upx)

```
in checkCache os.remove(cachedfile) WindowsError: [Error 2] The system cannot find the file specified: 'C:\Users\username\AppData\Roaming\pyinstaller\bincache01_py27_32bit\runw.exe'
```

Solution:

Update pip==8.0.3 and downgrade setuptools==19.2  ([ext-link](https://github.com/pyinstaller/pyinstaller/issues/1767))

Deleted the caching directory in %APPDATA%/pyinstaller  ([ext-link](https://groups.google.com/forum/#!msg/pyinstaller/oB-nY4imZXo/1zb2bJaOdZ0J))
