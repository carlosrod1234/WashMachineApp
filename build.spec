
# -*- mode: python -*-
a = Analysis(['Runtime.py'],
             pathex=['C:/Users/CARLOSPC/Documents/Python/Grancentrix/Grandcentrix/exec'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='GradcentrixApp.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='C:\\Users\\CARLOSPC\\Documents\\Python\\Grancentrix\\Grandcentrix\\py.ico')