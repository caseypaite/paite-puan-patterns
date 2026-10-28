#!/usr/bin/env python3
"""Export and package the Paite Puan Patterns skill for distribution.

Packages all skill assets, reference specifications, and documentation into a
self-contained, validated distribution archive (.zip) and directory.

Usage:
    python3 export_skill.py [--dest PATH] [--format {zip,dir,both}] [--verify-only]
"""

import argparse
from datetime import datetime
import hashlib
import json
import os
import shutil
import sys
import zipfile
from PIL import Image

SKILL_NAME = "paite-puan-patterns"
SKILL_AUTHOR = "Casey Paite"
PATTERNS = [
    ("paite-puandum", "01_Paite_Puandum.jpeg", "paite-puandum.jpg", "Paite Puandum"),
    ("siamsin-puan", "02_Siamsin_Puan.jpeg", "siamsin-puan.jpg", "Siamsin Puan"),
    ("thangsuah-puan", "03_Thangsuah_Puan.jpeg", "thangsuah-puan.jpg", "Thangsuah Puan"),
    ("puanlaisan", "04_Puanlaisan.jpeg", "puanlaisan.jpg", "Puanlaisan"),
    ("galhang-puan", "05_Galhang_Puan.jpeg", "galhang-puan.jpg", "Galhang Puan"),
    ("khephiau-puan", "06_Khephiau_Puan.jpeg", "khephiau-puan.jpg", "Khephiau Puan"),
    ("ngoutekhelh-puan", "07_Ngoutekhelh_Puan.jpeg", "ngoutekhelh-puan.jpg", "Ngoutekhelh Puan"),
    ("mal-am-puan", "08_Mal-am_Puan.jpeg", "mal-am-puan.jpg", "Mal-am Puan"),
    ("aksi-puan", "09_Aksi_Puan.jpeg", "aksi-puan.jpg", "Aksi Puan"),
    ("pangpalek-puan", "10_Pangpalek_Puan.jpeg", "pangpalek-puan.jpg", "Pangpalek Puan"),
    ("lianbuangthuam-puan", "11_Lianbuangthuam_Puan.jpeg", "lianbuangthuam-puan.jpg", "Lianbuangthuam Puan"),
    ("puanthupi-puan", "12_Puanthupi_Puan.jpeg", "puanthupi-puan.jpg", "Puanthupi Puan")
]

CREDIT_NOTICE = {
    "skill_author": "Casey Paite",
    "digital_artist": "Mr. Siam Naulak",
    "studio": "Naulak Web Design",
    "website": "https://naulak.com",
    "origin": "Created as design material for the 2027 Calendar of the Young Paite Association (YPA), West Delhi Unit.",
    "mandate": "Sacred traditional cultural patterns. Zero variations permitted. All reproductions must follow canonical pattern, color ratio, and order."
}


def sha256_file(filepath):
    """Compute sha256 checksum of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def find_skill_root():
    """Find the root directory of the paite-puan-patterns skill."""
    # Try directory of this script's parent
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    if os.path.exists(os.path.join(parent_dir, "SKILL.md")):
        return parent_dir

    # Fallback checks
    candidates = [
        os.path.join(os.getcwd(), "skills", SKILL_NAME),
        os.path.join(os.getcwd(), "puan-pattern"),
        os.path.join(os.getcwd(), SKILL_NAME),
        os.path.expanduser(f"~/.gemini/config/skills/{SKILL_NAME}")
    ]
    for c in candidates:
        if os.path.exists(os.path.join(c, "SKILL.md")):
            return c
    raise FileNotFoundError(f"Could not locate {SKILL_NAME} root directory.")


def verify_skill(skill_root):
    """Verify that all required files and assets exist and are valid."""
    errors = []
    warnings = []
    asset_manifest = []

    # 1. Verify SKILL.md
    skill_md = os.path.join(skill_root, "SKILL.md")
    if not os.path.exists(skill_md):
        errors.append("SKILL.md missing!")
    else:
        with open(skill_md, "r", encoding="utf-8") as f:
            content = f.read()
            if not content.startswith("---") or "name: paite-puan-patterns" not in content:
                errors.append("SKILL.md missing valid YAML frontmatter with name: paite-puan-patterns.")
            if "color ratio" not in content.lower() and "ratio" not in content.lower():
                warnings.append("SKILL.md should explicitly document color ratios.")
            if "order" not in content.lower():
                warnings.append("SKILL.md should explicitly document sequence order.")

    # 2. Verify references/pattern-catalog.md
    catalog_md = os.path.join(skill_root, "references", "pattern-catalog.md")
    if not os.path.exists(catalog_md):
        errors.append("references/pattern-catalog.md missing!")

    # 3. Verify assets/ and puan-images/
    assets_dir = os.path.join(skill_root, "assets")
    puan_images_dir = os.path.join(skill_root, "puan-images")

    if not os.path.exists(assets_dir):
        errors.append("assets/ directory missing!")
    if not os.path.exists(puan_images_dir):
        errors.append("puan-images/ directory missing!")

    for pid, canon_master, asset_img, name in PATTERNS:
        # Check standard asset
        asset_path = os.path.join(assets_dir, asset_img)
        if not os.path.exists(asset_path):
            errors.append(f"Standard asset missing for {name}: assets/{asset_img}")
        else:
            try:
                with Image.open(asset_path) as im:
                    im.verify()
                asset_manifest.append({
                    "id": pid,
                    "name": name,
                    "type": "standard_reference",
                    "path": f"assets/{asset_img}",
                    "size_bytes": os.path.getsize(asset_path),
                    "sha256": sha256_file(asset_path)
                })
            except Exception as e:
                errors.append(f"Corrupt standard asset image {asset_img}: {e}")

        # Check master graphic image in puan-images
        master_path = os.path.join(puan_images_dir, canon_master)
        if not os.path.exists(master_path):
            errors.append(f"Master graphic image missing for {name}: puan-images/{canon_master}")
        else:
            try:
                with Image.open(master_path) as im:
                    dim = im.size
                asset_manifest.append({
                    "id": pid,
                    "name": name,
                    "type": "master_graphic",
                    "path": f"puan-images/{canon_master}",
                    "resolution": f"{dim[0]}x{dim[1]}",
                    "size_bytes": os.path.getsize(master_path),
                    "sha256": sha256_file(master_path)
                })
            except Exception as e:
                errors.append(f"Corrupt master graphic image {canon_master}: {e}")

    # 4. Verify puan-images/INDEX.md
    index_md = os.path.join(puan_images_dir, "INDEX.md")
    if not os.path.exists(index_md):
        warnings.append("puan-images/INDEX.md missing.")

    return errors, warnings, asset_manifest


def build_package(skill_root, dest_path, fmt="both"):
    """Package the skill and all assets into a zip archive and/or directory."""
    errors, warnings, asset_manifest = verify_skill(skill_root)
    if errors:
        print("Verification failed with errors:")
        for e in errors:
            print(f"  ❌ {e}")
        return False

    if warnings:
        print("Warnings during verification:")
        for w in warnings:
            print(f"  ⚠️ {w}")

    # Create destination directory
    dest_dir = os.path.abspath(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    dist_skill_dir = os.path.join(dest_dir, SKILL_NAME)
    zip_path = os.path.join(dest_dir, f"{SKILL_NAME}.zip")

    # Generate Manifest
    manifest_data = {
        "skill_name": SKILL_NAME,
        "author": SKILL_AUTHOR,
        "version": "2.0.0",
        "packaged_at": datetime.now().isoformat(),
        "zero_variation_mandate": True,
        "cultural_integrity": "Paite Puan patterns are canonical traditional cloths. Variations, arbitrary recoloring, or pattern alterations are prohibited.",
        "credits": CREDIT_NOTICE,
        "pattern_count": len(PATTERNS),
        "patterns": [p[3] for p in PATTERNS],
        "assets": asset_manifest
    }

    if fmt in ("dir", "both"):
        if os.path.exists(dist_skill_dir):
            shutil.rmtree(dist_skill_dir)
        os.makedirs(dist_skill_dir, exist_ok=True)

        # Copy SKILL.md
        shutil.copy2(os.path.join(skill_root, "SKILL.md"), dist_skill_dir)

        # Copy references/
        shutil.copytree(os.path.join(skill_root, "references"),
                        os.path.join(dist_skill_dir, "references"))

        # Copy assets/ (dereferencing symlinks so all files are self-contained)
        os.makedirs(os.path.join(dist_skill_dir, "assets"), exist_ok=True)
        assets_src = os.path.join(skill_root, "assets")
        for item in os.listdir(assets_src):
            s = os.path.join(assets_src, item)
            d = os.path.join(dist_skill_dir, "assets", item)
            if os.path.isfile(s) or (os.path.islink(s) and os.path.isfile(os.path.realpath(s))):
                shutil.copy2(os.path.realpath(s), d)

        # Copy puan-images/ (dereferencing symlinks)
        os.makedirs(os.path.join(dist_skill_dir, "puan-images"), exist_ok=True)
        puan_src = os.path.join(skill_root, "puan-images")
        for item in os.listdir(puan_src):
            s = os.path.join(puan_src, item)
            d = os.path.join(dist_skill_dir, "puan-images", item)
            if os.path.isfile(s) or (os.path.islink(s) and os.path.isfile(os.path.realpath(s))):
                shutil.copy2(os.path.realpath(s), d)

        # Copy scripts/
        scripts_src = os.path.join(skill_root, "scripts")
        if os.path.exists(scripts_src):
            shutil.copytree(scripts_src, os.path.join(dist_skill_dir, "scripts"))

        # Save manifest
        with open(os.path.join(dist_skill_dir, "MANIFEST.json"), "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=2)

        print(f"✅ Packaged directory: {dist_skill_dir}")

    if fmt in ("zip", "both"):
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            # 1. SKILL.md
            zf.write(os.path.join(skill_root, "SKILL.md"), f"{SKILL_NAME}/SKILL.md")

            # 2. references/
            ref_dir = os.path.join(skill_root, "references")
            for root, _, files in os.walk(ref_dir):
                for file in files:
                    full = os.path.join(root, file)
                    rel = os.path.relpath(full, skill_root)
                    zf.write(full, f"{SKILL_NAME}/{rel}")

            # 3. assets/
            assets_dir = os.path.join(skill_root, "assets")
            for item in os.listdir(assets_dir):
                full = os.path.join(assets_dir, item)
                if os.path.isfile(full) or (os.path.islink(full) and os.path.isfile(os.path.realpath(full))):
                    zf.write(os.path.realpath(full), f"{SKILL_NAME}/assets/{item}")

            # 4. puan-images/
            puan_dir = os.path.join(skill_root, "puan-images")
            for item in os.listdir(puan_dir):
                full = os.path.join(puan_dir, item)
                if os.path.isfile(full) or (os.path.islink(full) and os.path.isfile(os.path.realpath(full))):
                    zf.write(os.path.realpath(full), f"{SKILL_NAME}/puan-images/{item}")

            # 5. scripts/
            scripts_dir = os.path.join(skill_root, "scripts")
            if os.path.exists(scripts_dir):
                for root, _, files in os.walk(scripts_dir):
                    for file in files:
                        full = os.path.join(root, file)
                        rel = os.path.relpath(full, skill_root)
                        zf.write(full, f"{SKILL_NAME}/{rel}")

            # 6. MANIFEST.json
            zf.writestr(f"{SKILL_NAME}/MANIFEST.json", json.dumps(manifest_data, indent=2))

        print(f"✅ Packaged ZIP archive: {zip_path} ({os.path.getsize(zip_path):,} bytes)")

    return True


def main():
    parser = argparse.ArgumentParser(description="Export and package Paite Puan Patterns skill.")
    parser.add_argument("--dest", default=None, help="Destination directory for distribution bundle.")
    parser.add_argument("--format", choices=["zip", "dir", "both"], default="both", help="Export format.")
    parser.add_argument("--verify-only", action="store_true", help="Run verification without creating bundle.")
    args = parser.parse_args()

    skill_root = find_skill_root()
    print(f"Skill root: {skill_root}")

    if args.verify_only:
        errors, warnings, manifest = verify_skill(skill_root)
        print(f"Assets checked: {len(manifest)}")
        if errors:
            print("Errors:")
            for e in errors:
                print(f"  ❌ {e}")
            sys.exit(1)
        if warnings:
            print("Warnings:")
            for w in warnings:
                print(f"  ⚠️ {w}")
        print("✅ Skill verification successful. All assets and specifications valid.")
        sys.exit(0)

    dest_dir = args.dest
    if not dest_dir:
        # Default destination: skills/dist or dist
        dest_dir = os.path.join(os.path.dirname(skill_root), "dist")

    success = build_package(skill_root, dest_dir, fmt=args.format)
    if not success:
        sys.exit(1)
    print("\n🎉 Skill export completed successfully.")


if __name__ == "__main__":
    main()
