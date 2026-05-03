
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['APP/src/main.py'],
    pathex=['.'],
    datas=[('APP/models','models'),('APP/web','web')],
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name='MyEnterpriseXMLApp',
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    name='MyEnterpriseXMLApp'
)
