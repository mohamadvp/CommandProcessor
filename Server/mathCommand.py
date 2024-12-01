import math
import re

def math_command(command_data):
    expression = command_data.get("expression")
    
    if not expression:
        return {"status": "error", "output": "Missing expression field"}
    if not re.search(r"[+\-*/%^()]|/d/s+/d", expression):
        return {"status": "error", "output": "Invalid mathematical operation"}
    if re.search(r"[+\-*/%^]$", expression.strip()):
        return {"status": "error", "output": "Expression ends with an operator"}
    try:
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return {"status": "success", "output": result}
    except Exception as e:
        return {"status": "error", "output": str(e)}
