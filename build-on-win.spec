# -*- mode: python -*-

block_cipher = None

a = Analysis(['tasmota-pyflasher.py'],
             binaries=[],
             datas=[("images", "images")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Tasmota-PyFlasher-1.0',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='images\\icon-256.ico')
