def ping(host):
    os.system("ping " + host)  # UNSAFE
    print("Command Injection")