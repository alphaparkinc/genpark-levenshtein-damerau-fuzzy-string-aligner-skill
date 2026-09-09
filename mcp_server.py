"""MCP Server for Damerau-Levenshtein Skill."""
import json
import sys
from client import DamerauLevenshtein

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "compute_edit_distance",
                            "description": "Calculate Damerau-Levenshtein edit distance",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "str1": {"type": "string"},
                                    "str2": {"type": "string"}
                                },
                                "required": ["str1", "str2"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                d = DamerauLevenshtein.distance(args["str1"], args["str2"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"distance": d})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
