from collections import defaultdict

def basic_triage(failures):
    buckets = defaultdict(list)
for f in failures:
    key = (f.get('test','unknown'), f.get('message','unknown')[:80])
buckets[key].append(f)
clusters = [
    {
        "test": k[0],
        "signature": k[1],
        "count": len(v),
        "examples": v[:3]
    } for k, v in buckets.items()
]
clusters.sort(key=lambda x: x["count"], reverse=True)
summary = f"{len(failures)} failures clustered into {len(clusters)} groups"
return {"summary": summary, "clusters": clusters}