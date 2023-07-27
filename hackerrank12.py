def wrapper(f):
    def fun(l):
        listPhone = []
        # complete the function
        for i in l : 
            listPhone.append(f'+91 {i[-10:-5]} {i[-5::]}')
        f(listPhone)
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

    # Decorator question of phone number 
    