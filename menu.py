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
    menu_select = input()
    provider = ""
    try:
        value = int(menu_select)
        if value is 1:
            provider = "AWS"
        elif value is 2:
            provider = "IBM Cloud"
        elif value is 3:
            provider = "Verizon Cloud"
        elif value is 4:
            provider = "Kamatera"
        elif value is 5:
            provider = "Vultr"
        elif value is 6:
            provider = "Rackspace"
        elif value is 7:
            provider = "Salesforce"
        elif value is 8:
            provider = "M247"
        elif value is 9:
            provider = "Tencent Cloud"
        elif value is 10:
            provider = "Alibaba Cloud"
        elif value is 11:
            provider = "Baidu"
        else:
            print("Invalid menu option selection entered")
            provider = ""
        return provider
    except ValueError:
        print("Please select a number representing a provider as shown on the menu")


if __name__ == "__main__":
    chosen = menu()
    print("Viewing: ", chosen)
