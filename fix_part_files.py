import glob

for fname in glob.glob("build_sb_part*.py") + ["build_statement_based_repository.py"]:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace open with exists check or init
    target_str = """with open(target_path, "r", encoding="utf-8") as f:
    questions = json.load(f)"""
    
    replacement_str = """if target_path.exists():
    try:
        with open(target_path, "r", encoding="utf-8") as f:
            questions = json.load(f)
    except Exception:
        questions = []
else:
    questions = []"""
    
    if target_str in content:
        content = content.replace(target_str, replacement_str)
        with open(fname, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {fname}")

print("Done fixing files.")
