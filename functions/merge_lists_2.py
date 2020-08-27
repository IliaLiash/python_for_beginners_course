def quick_merge(amount):
    main_list = []
    for i in range(amount):
        main_list.extend([i for i in input().split()])    
    for i in range(len(main_list)):
        main_list[i] = int(main_list[i])        
    
    return sorted(main_list)

n = int(input())

print(*quick_merge(n))
