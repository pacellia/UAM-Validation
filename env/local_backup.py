from pathlib import Path
import shutil, argparse, json, datetime
from datetime import UTC

def main():
    ap = argparse.ArgumentParser(description='Copy archives to local HDD')
    ap.add_argument('--src', default='/content/drive/MyDrive/UAM_Public/archives', help='Source archives dir')
    ap.add_argument('--dest', required=True, help='Destination HDD path')
    args = ap.parse_args()
    src = Path(args.src); dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    copied = []
    for p in src.glob('*.zip'):
        tgt = dest/p.name
        shutil.copy2(p, tgt)
        copied.append({'name': p.name, 'bytes': p.stat().st_size})
        print(f"[copy] {p} -> {tgt}")
    manifest = {
        'timestamp': datetime.datetime.now(UTC).isoformat(),
        'src': str(src), 'dest': str(dest), 'count': len(copied), 'files': copied,
    }
    (dest/'backup_manifest.json').write_text(json.dumps(manifest, indent=2))
    print(f"[done] {len(copied)} files copied. Manifest written to {dest/'backup_manifest.json'}")

if __name__ == '__main__':
    main()
