import platform
import subprocess
from dangerousCommand import dangerous_commands

def os_command(command_data):
    command_name = command_data.get("command_name")
    parameters = command_data.get("parameters", [])

    current_platform = platform.system().lower()
    platform_key = "linux" if current_platform == "linux" else "windows"
    blocked_commands = dangerous_commands.get(platform_key, [])
    if command_name in blocked_commands:
        return {"status": "confirm", "message": f"Command '{command_name}' is potentially dangerous. Confirm to proceed"}

    try:
        if not command_name:
            return {"status": "error", "output": "Missing command_name field"}

        command = [command_name] + parameters

        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            return {"status": "success", "output": result.stdout.strip()}
        else:
            return {"status": "error", "output": result.stderr.strip()}
    except Exception as e:
        return {"status": "error", "output": str(e)}