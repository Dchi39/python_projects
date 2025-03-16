import time

def brewCoffee():
    print("Start brewing coffee...")
    time.sleep(3)
    print("End brewCoffee")
    return "Coffee ready"

def toastBegele():
    print("Start toasting begele...")
    time.sleep(2)
    print("End toastBegele")
    return "Begele toasted"

def main():
    start_time = time.time()

    result_coffee = brewCoffee()
    result_begele = toastBegele()
    end_time = time.time()
    elased_time = end_time - start_time

    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBegele: {result_begele}")
    print(f"Total time: {elased_time:.2f} seconds")

if __name__ == "__main__":
    main()