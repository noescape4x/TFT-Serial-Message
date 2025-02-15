import tkinter as tk
import serial
import serial.tools.list_ports

def send_message():
    message = entry.get()
    if ser and ser.is_open:
        ser.write((message + '\n').encode('utf-8'))
        status_label.config(text=f"Sent: {message}", fg="green")
    else:
        status_label.config(text="Error: Serial not connected", fg="red")

def refresh_ports():
    ports = get_serial_ports()
    port_menu['menu'].delete(0, 'end')
    for p in ports:
        port_menu['menu'].add_command(label=p, command=lambda value=p: selected_port.set(value))
    if ports:
        selected_port.set(ports[0])

def connect_serial():
    global ser
    try:
        ser = serial.Serial(selected_port.get(), 9600, timeout=1)
        status_label.config(text=f"Connected to {selected_port.get()}", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")

def get_serial_ports():
    return [port.device for port in serial.tools.list_ports.comports()]

# GUI Setup
root = tk.Tk()
root.title("Arduino Message Sender")
root.geometry("400x250")

selected_port = tk.StringVar()
port_label = tk.Label(root, text="Select Serial Port:")
port_label.pack()
port_menu = tk.OptionMenu(root, selected_port, *get_serial_ports())
port_menu.pack()
refresh_button = tk.Button(root, text="Refresh Ports", command=refresh_ports)
refresh_button.pack()
connect_button = tk.Button(root, text="Connect", command=connect_serial)
connect_button.pack()

label = tk.Label(root, text="Enter Message:")
label.pack()
entry = tk.Entry(root, width=40)
entry.pack()
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

status_label = tk.Label(root, text="", fg="black")
status_label.pack()

ser = None
refresh_ports()
root.mainloop()

if ser and ser.is_open:
    ser.close()