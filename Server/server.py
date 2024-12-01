import json
import zmq
from osCommand import os_command
from mathCommand import math_command
from logger import log_error, log_info, log_success


def process_command(command):
    try:
        if command["command_type"] == "os":
            return os_command(command)
        elif command["command_type"] == "compute":
            return math_command(command)
        else:
            return {"status": "error", "output": f"Invalid command type"}
    except Exception as e:
        log_error(f"Error processing command: {e} ")
        return {"status": "error", "output": str(e)}


def server():
    context = zmq.Context()
    socket = context.socket(zmq.ROUTER)
    socket.bind("tcp://*:5555")
    log_info("Server is running....")

    while True:
        try:
            client_id, message = socket.recv_multipart()
            message = json.loads(message.decode("utf-8"))
            log_info(f"Received from client {client_id}:\n{message}")

            response = process_command(message)
            if response["status"] == 'error':
                log_error(f"Failed to processed command: {response["output"]}")
            else:
                log_success(f"Successfully processed command: \n{response["output"]}")

            socket.send_multipart(
                [client_id, json.dumps(response).encode("utf-8")])
        except Exception as e:
            log_error(f"Failed to processed command: {str(e)}")


if __name__ == "__main__":
    server()
