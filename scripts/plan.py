"""Print "<path of video.mp4> <unit id>" for every unit of the subjects that
learning-app's content/video-hosts.yaml assigns to this site."""
import sys
from pathlib import Path
import yaml

src = Path(sys.argv[1])
cfg_file = src / 'content/video-hosts.yaml'
cfg = (yaml.safe_load(cfg_file.read_text(encoding='utf-8')) or {}) if cfg_file.exists() else {}
site = 'https://adazakuraa.github.io/learning-app-2'
subjects = {s for h in cfg.get('external', []) if h.get('base', '').rstrip('/') == site for s in h.get('subjects', [])}
for sy in sorted((src / 'content').glob('*/subject.yaml')):
    if (yaml.safe_load(sy.read_text(encoding='utf-8')) or {}).get('id') not in subjects:
        continue
    for uy in sorted(sy.parent.glob('*/*/unit.yaml')):
        unit = yaml.safe_load(uy.read_text(encoding='utf-8')) or {}
        if (unit.get('video') or {}).get('src') == 'video.mp4':
            print(f"{uy.parent.relative_to(src)}/video.mp4 {unit['id']}")
