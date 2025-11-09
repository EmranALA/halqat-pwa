import os, json

manifest_path = "app/manifest.json"
page_url = os.environ.get("GITHUB_PAGES_URL")

if not os.path.exists(manifest_path):
    print(f"manifest.json not found at {manifest_path}")
    exit(1)

with open(manifest_path, "r+", encoding="utf-8") as f:
    try:
        m = json.load(f)
    except Exception:
        m = {}

    m["start_url"] = page_url
    m["id"] = page_url
    m["scope"] = page_url

    if "icons" in m:
        for ic in m["icons"]:
            src = ic.get("src", "")
            if src and not src.startswith("http"):
                ic["src"] = page_url.rstrip("/") + "/" + src.lstrip("/")

    f.seek(0)
    f.truncate()
    json.dump(m, f, ensure_ascii=False, indent=2)

print("manifest.json updated successfully.")
