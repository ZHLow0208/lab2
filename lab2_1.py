import statistics as st

def main():
 print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
 display_main_menu()
 num_list = [float(item) for item in get_user_input()]
 print(find_min_max(num_list))
 print(sort_temperature(num_list))
 print(calc_median_temperature(num_list))
 print(calc_average(num_list))

def display_main_menu():
 print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def calc_average(x):
 y = st.mean(x)
 return y

def get_user_input():
 x = input().split(",")
 return x
def find_min_max(x):
 max_temp = max(x)
 min_temp = min(x)
 return [max_temp,min_temp]
def sort_temperature(x):
 y = sorted(x,reverse=False)
 return y
def calc_median_temperature(x):
 num_median = st.median(x)
 return num_median

if __name__ == "__main__":
 main()

