from app.services.diff_parser import parse_diff
from app.services.llm_parser import review_code

sample_diff = """diff --git a/app/utils.py b/app/utils.py
index 83db48f..f735c2a 100644
--- a/app/utils.py
+++ b/app/utils.py
@@ -1,7 +1,8 @@
 def calculate_total(items):
-    total = 0
-    for item in items:
-        total = total + item
-    return total
+    if not items:
+        return 0
+    return sum(items)
"""

parsed = parse_diff(sample_diff)
for file_data in parsed:
    review = review_code(file_data)
    print(review)