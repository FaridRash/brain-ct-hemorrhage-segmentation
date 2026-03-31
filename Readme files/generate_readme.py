import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(BASE_DIR, "project.json")
readme_path = os.path.join(BASE_DIR, "README.md")

with open(json_path, encoding="utf-8") as f:
    data = json.load(f)

md = ""

# ---- TITLE ----
md += f"# 🧠 {data['title']}\n\n"

# ---- PROJECT VISION ----
pv = data["project_vision"]
md += "## 🚀 Project Vision\n\n"
md += pv["description"] + "\n\n"

md += "**Architecture:**\n"
md += f"- {pv['architecture']}\n\n"

md += "**Long-term Goal:**\n"
md += f"- {pv['long_term_goal']}\n\n"

md += "**Components:**\n"
for c in pv["components"]:
    md += f"- {c}\n"
md += "\n"

# ---- CURRENT FOCUS ----
cf = data["current_focus"]
md += "## 📌 Current Focus\n\n"
md += f"**Version:** {cf['version']}\n\n"
md += f"{cf['goal']}\n\n"

for t in cf["tasks"]:
    md += f"- {t}\n"
md += "\n"

# ---- ARCHITECTURE ----
md += "## 🧩 System Architecture\n\n"
for step in data["system_architecture"]:
    md += f"{step}\n↓\n"
md += "\n"

# ---- DATASET ----
ds = data["dataset"]
md += "## 📊 Dataset\n\n"
md += f"**{ds['name']}**\n\n"
md += f"{ds['url']}\n\n"

for d in ds["details"]:
    md += f"- {d}\n"

md += f"\n⚠️ {ds['note']}\n\n"

# ---- IMPLEMENTED ----
imp = data["implemented"]
md += "## ⚙️ Implemented Pipeline\n\n"

md += "### Conversion\n"
md += f"- {imp['conversion']['description']}\n"
for a in imp["conversion"]["alignment"]:
    md += f"- {a}\n"
md += "\n"

md += "### Data Format\n"
df = imp["data_format"]
md += f"- Removed: {df['removed']}\n"
md += f"- Used: {df['used']}\n"
md += f"- Reason: {df['reason']}\n"
for b in df["benefits"]:
    md += f"- {b}\n"
md += "\n"

md += "### Labeling\n"
lab = imp["labeling"]
md += f"- Method: {lab['method']}\n"
md += f"- Logic: `{lab['logic']}`\n"
md += f"- Output: {lab['output']}\n\n"

md += "### Preprocessing\n"
pre = imp["preprocessing"]
for s in pre["steps"]:
    md += f"- {s}\n"
md += f"\n⚠️ {pre['important_note']}\n\n"

md += "### Dataset Split\n"
split = imp["dataset_split"]
dist = split["distribution"]
md += f"- Method: {split['method']}\n"
md += f"- Reason: {split['reason']}\n"
md += f"- Train: {dist['train']}\n"
md += f"- Val: {dist['val']}\n"
md += f"- Test: {dist['test']}\n\n"

md += "### Data Structure\n"
struct = imp["data_structure"]
md += f"{struct['root']}/\n"
for k, v in struct["structure"].items():
    md += f"  {k}/\n"
    for item in v:
        md += f"    - {item}\n"
md += "\n"

md += "### Validation\n"
for v in imp["validation"]:
    md += f"- {v}\n"
md += "\n"

# ---- INPUT OUTPUT ----
io = data["input_output"]
md += "## 📥 Input / Output\n\n"
md += f"**Input:** {io['input']}\n\n"
md += "**Output:**\n"
for o in io["output"]:
    md += f"- {o}\n"
md += "\n"

# ---- METRICS ----
metrics = data["evaluation_metrics"]
md += "## 📈 Evaluation Metrics\n\n"

md += "### Classification\n"
for m in metrics["classification"]:
    md += f"- {m}\n"

md += "\n### Segmentation\n"
for m in metrics["segmentation"]:
    md += f"- {m}\n"
md += "\n"

# ---- STATUS ----
status = data["current_status"]
md += "## 📌 Current Status\n\n"

md += "### Completed\n"
for c in status["completed"]:
    md += f"- {c}\n"

md += "\n### Next Steps\n"
for n in status["next_steps"]:
    md += f"- {n}\n"
md += "\n"

# ---- FUTURE WORK ----
fw = data["future_work"]
md += "## 🔮 Future Work\n\n"

for key, values in fw.items():
    md += f"### {key}\n"
for v in values:
    md += f"- {v}\n"
md += "\n"

# ---- TEAM ----
team = data["team_structure"]
md += "## 🤝 Team Structure\n\n"
for m in team["modules"]:
    md += f"- **{m['name']}**: {m['description']}\n"
md += "\n"

# ---- KEY FOCUS ----
md += "## 🧠 Key Focus\n\n"
for k in data["key_focus"]:
    md += f"- {k}\n"
md += "\n"

# ---- DISCLAIMER ----
md += "## ⚠️ Disclaimer\n\n"
md += data["disclaimer"] + "\n\n"

# ---- CONTACT ----
md += "## 📬 Contact\n\n"
md += data["contact"]["note"] + "\n"

# ---- SAVE ----
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(md)

print("✅ README.md generated successfully")