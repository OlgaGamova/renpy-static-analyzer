"""Debug test to see what API returns."""

from core.api import analyze_script, ScriptRequest

code = """label start:
    "Hello"
    call missing_label
    return
    jump end
    
label end:
    "End"
"""

req = ScriptRequest(code=code)
result = analyze_script(req)

print("Result keys:", result.keys())
print("\nAnalysis keys:", result.get("analysis", {}).keys())
print("\nErrors:", result.get("error", "No errors"))
print("\nWarnings:", result.get("analysis", {}).get("warnings", "NO WARNINGS KEY"))

if "error" in result:
    print("\nFull error:", result["error"])
