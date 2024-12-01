import zmq

def send_command(socket,command):
    socket.send_json(command)
    response = socket.recv_json()
    return response

def client():
    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    socket.connect("tcp://localhost:5555")
    print("Client is running ....")

    while True:
        print(f"1: Os Command\n2: Math Command\n3: Exit")
        
        choice = input("Enter your Choice: ")
        if choice == "1":
            command_name = input("Enter Os command: ").lower()
            Parameters = input("Enter parameters: ").split()
            command= {
                "command_type":"os",
                "command_name":command_name,
                "parameters":Parameters,
            }
        elif choice == "2": 
            expression = input("Enter math expression: ")
            command = {
                "command_type": "compute",
                "expression": expression
            }
        elif choice == "3":
             break
        else:
             print("Invalid choice. Please select a valid option from the menu.")
             continue
                
        response = send_command(socket,command)
        
        if response["status"] == "confirm":
            print(response["message"])
            confirm = input("Do you want to proceed? (yes/no): ").strip().lower()
            if confirm == "yes":
                response = send_command(command)
            else:
                print("Command execution cancelled.")
        else:
            print("Response:")
            print(f"status: {response["status"]} \noutput: {response["output"]}")

if __name__ == "__main__":
    client()