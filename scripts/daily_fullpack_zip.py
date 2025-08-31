# Template: zip the entire /content/notebook tree and drop into Drive mirror archives
    from pathlib import Path
    import zipfile, hashlib, time, os

    PROJ = Path('/content/notebook')
    ARCH = Path('/content/drive/MyDrive/UAM_Public/archives')
    ARCH.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime('%Y%m%d_%H%M%S')
    out = ARCH / f'UAM_fullpack_{stamp}.zip'

    def sha256_file(p: Path) -> str:
        h = hashlib.sha256()
        with open(p, 'rb') as f:
            for chunk in iter(lambda: f.read(1<<20), b''):
                h.update(chunk)
        return h.hexdigest()

    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zh:
        for root, _, files in os.walk(PROJ):
            for name in files:
                p = Path(root)/name
                arc = p.relative_to(PROJ)
                zh.write(p, f'notebook/{arc}')

    print('[zip]', out)
    print('[sha256]', sha256_file(out))
