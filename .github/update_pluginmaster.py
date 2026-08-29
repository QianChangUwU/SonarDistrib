import json
import os
import sys
import time

repo_path = sys.argv[1]       # dalamud-plugins checkout
version = sys.argv[2]         # e.g. 15.755.2.0
repo_full_name = sys.argv[3]  # e.g. QianChangUwU/SonarDistrib
manifest_path = sys.argv[4]   # e.g. release/SonarPlugin.json

json_path = os.path.join(repo_path, 'pluginmaster.json')

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

download_url = f"https://github.com/{repo_full_name}/releases/download/v{version}/latest.zip"

internal_name = manifest.get('InternalName', 'SonarPlugin')

entry = {
    'Author': manifest.get('Author', 'Sonar Team'),
    'Name': manifest.get('Name', 'Sonar'),
    'InternalName': internal_name,
    'AssemblyVersion': version,
    'TestingAssemblyVersion': version,
    'DalamudApiLevel': 15,
    'TestingDalamudApiLevel': 15,
    'DownloadLinkInstall': download_url,
    'DownloadLinkUpdate': download_url,
    'DownloadLinkTesting': download_url,
    'RepoUrl': manifest.get('RepoUrl', f'https://github.com/{repo_full_name}'),
    'IconUrl': manifest.get('IconUrl', download_url),
    'ImageUrls': manifest.get('ImageUrls', []),
    'Punchline': manifest.get('Punchline', ''),
    'Description': manifest.get('Description', ''),
    'Changelog': manifest.get('Changelog', ''),
    'Tags': manifest.get('Tags', []),
    'CategoryTags': manifest.get('CategoryTags', []),
    'ApplicableVersion': manifest.get('ApplicableVersion', 'any'),
    'LoadPriority': manifest.get('LoadPriority', 0),
    'AcceptsFeedback': manifest.get('AcceptsFeedback', False),
    'LastUpdate': int(time.time()),
}

existing = next((e for e in data if e.get('InternalName') == internal_name), None)
if existing is not None:
    existing.update(entry)
else:
    data.append(entry)

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Updated pluginmaster.json entry for {internal_name} v{version}")
