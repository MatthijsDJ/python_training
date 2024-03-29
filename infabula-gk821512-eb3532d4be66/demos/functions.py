nerderig_number = 42

def change_nerdy(nerderig_number):
    #global nerderig_number  # <--------
    nerderig_number = 0
    print(nerderig_number)  # 0
    return nerderig_number

def main():
    print(nerderig_number)  # 42
    nerderig_number = 42
    nerderig_number = change_nerdy(nerderig_number)
    print(nerderig_number)

main()