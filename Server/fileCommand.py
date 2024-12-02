import os


def file_command(command_data):
    path = command_data["path"]
    operation = command_data["operation"]
    if not path or not operation:
        return {"status": "error", "output": "Missing required fields: 'operation' or 'path'"}
    if not os.path.exists(path):
        return {"status": "error", "output": f"Path '{path}' does not exits"}

    try:
        if operation == "read":
            with open(path, "r") as file:
                file_content = file.read()
                return {"status": "success", "output": f"File content:\n{str(file_content)}"}
        elif operation == "write":
            content = command_data["content"]
            with open(path, "w") as file:
                file.write(content)
                return {"status": "success", "output": f"Content written to '{path}' successfully"}
        elif operation == "append":
            content = command_data["content"]
            with open(path, "a") as file:
                file.write(f"\n{content}")
                return {"status": "success", "output": f"Content append to '{path}' successfully"}
        elif operation == "list":
            file = os.listdir(path)
            return{"status":"success","output":f"Files:\n{"\n".join(file)}"}
        elif operation == "delete":
            os.remove(path)
            return{"status": "success", "output":f"File '{path}' deleted successfully"}
        else:
            return {"status": "error", "output": f"Unsupported operation: {operation}"}
        return {"status": "success", "output": "success"}
    except Exception as e:
        return {"status": "error", "output": str(e)}
