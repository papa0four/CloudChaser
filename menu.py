def menu():
    print("Please select a Provider from the following menu options:")
    print("1.\tAWS")
    print("2.\tIBM Cloud")
    print("3.\tVerizon Cloud")
    print("4.\tKamatera")
    print("5.\tVultr")
    print("6.\tRackspace")
    print("7.\tSalesforce")
    print("8.\tM247")
    print("9.\tTencent Cloud")
    print("10.\tAlibaba Cloud")
    print("11.\tBaidu")
    print("12.\tMicrosoft Azure")
    print("13.\tGoogle Cloud Platform")
    menu_select = input("/> ")
    provider = ""
    try:
        value = int(menu_select)
        if value == 1:
            provider = "AWS"
        elif value == 2:
            provider = "IBM Cloud"
        elif value == 3:
            provider = "Verizon Cloud"
        elif value == 4:
            provider = "Kamatera"
        elif value == 5:
            provider = "Vultr"
        elif value == 6:
            provider = "Rackspace"
        elif value == 7:
            provider = "Salesforce"
        elif value == 8:
            provider = "M247"
        elif value == 9:
            provider = "Tencent Cloud"
        elif value == 10:
            provider = "Alibaba Cloud"
        elif value == 11:
            provider = "Baidu"
        elif value == 12:
            provider = "Microsoft Azure"
        elif value == 13:
            provider = "Google Cloud Platform"
        else:
            print("Invalid menu option selection entered")
            provider = "Error: Menu Option Invalid"
        return provider
    except ValueError:
        print("Please select a number representing a provider as shown on the menu")


if __name__ == "__main__":
    chosen = menu()
    print("Viewing: ", chosen)
