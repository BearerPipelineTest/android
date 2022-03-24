#!/usr/bin/env python3
import xml.etree.ElementTree as ET
category_counts = {}
category_names = {}
tree = ET.parse("app/build/reports/spotbugs/gplayDebug.xml")

for child in tree.getroot():
    if child.tag == "BugInstance":
        category = child.attrib['category']
        if category in category_counts:
            category_counts[category] = category_counts[category] + 1
        else:
            category_counts[category] = 1
    elif child.tag == "BugCategory":
        category = child.attrib['category']
        category_names[category] = child[0].text

print("Category|Count")
print("---|---")

categories = sorted(category_counts.keys())
for category in categories:
    print(f"{category_names[category]}|{category_counts[category]}")

print(f"**Total**|**{sum(category_counts.values())}**")