# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/anura/Desktop/Hospital-Management-Software/Hospital-Management-Software/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/anura/Desktop/Hospital-Management-Software/Hospital-Management-Software/log_in.kv', '.'), ('C:/Users/anura/Desktop/Hospital-Management-Software/Hospital-Management-Software/main.kv', '.'), ('C:/Users/anura/Desktop/Hospital-Management-Software/Hospital-Management-Software/sign_in.kv', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
