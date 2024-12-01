# Command Processor with ZeroMQ

##  Description

This project implements a **client-server application** using **ZeroMQ** for communication. The server processes two types of commands:

1. **OS Commands**: Executes system commands such as `ping` or listing directories.
2. **Math Commands**: Evaluates mathematical expressions using Python’s `math` module.

The project supports multiple clients concurrently.


##  Features

- Identify the type of command
- Execute **OS commands** and return results.
- Evaluate **mathematical expressions** safely.
- Asks for user confirmation if input dangerous OS commands in windows and linux
- Supports **multiple clients** using **zmq.ROUTER** and **zmq.DEALER**
- Implements **error handling** for invalid inputs from Client.
- Implements **error handling** for math and os commands.
- Implement command **logging** on the server.


## Project Structure

The project is organized as follows:

```
.
├── server/                 
│   ├── dangerousCommand.py           
│   ├── logger.py
│   ├── mathCommand.py        
│   ├── osCommand.py      
│   ├── server.py 
├── client/                 
│   └── client.py           
├── README.md               

```

##  Installation

### To run this project, you need to have Python installed with the following dependencies:

### platform, subprocess, math (Python library).

### pyzmq: Python bindings for ZeroMQ.
```bash
pip install pyzmq
```

### Run the Server: Start the server to listen for client requests:
```bash
python Server/server.py
```

### Run the Client: Launch the client to send commands to the server:
```bash
python Client/client.py
```


# Usage

### Client Menu

Once the client starts, the following menu is displayed:
```bash
1: OS Command
2: Math Command
3: Exit
```

## Examples
### OS Command Example

### Input:
```bash
{
  "command_type": "os",
  "command_name": "ping",
  "parameters": ["127.0.0.1", "-n", "4"]
}
```
### Output:
```bash
{
  "status": "success",
  "output": "Pinging 127.0.0.1 with 32 bytes of data..."
}

```
### Math Command Example
### Input:
```bash
{
  "command_type": "compute",
  "expression": "(3 + 5) * 2"
}
```
### Output:
```bash
{
  "status": "success",
  "output": 16
}
```
### Dangerous Commands
Commands such as rm -rf or del are dangerous. The server requires confirmation before executing these commands.

### Server Response:
```bash
{
  "status": "confirm",
  "message": "Command 'rm' is potentially dangerous. Confirm to proceed"
}
```
If the user confirms, the command executes. Otherwise, it is canceled.

#  Design and Architecture
### Server
The server processes incoming commands from clients and executes them. The server can handle both OS commands and Math commands:

For OS commands, the server uses the subprocess library to execute the commands and capture the output.
For Math commands, the server evaluates mathematical expressions using Python's eval function, ensuring only safe built-in functions from the math module are available.

### Client
The client sends commands to the server over ZeroMQ using zmq.REQ sockets. It allows users to input either OS commands or Math expressions and displays the response from the server.

### Handling Multiple Clients
The server is designed to handle multiple clients by using zmq.ROUTER and zmq.DEALER sockets for scalable and efficient communication. This enables the server to handle concurrent requests and maintain responsiveness.

#  Contact
### Name: Mohammadreza Sharif
### Email: s.mohammadreza.lol@gmail.com