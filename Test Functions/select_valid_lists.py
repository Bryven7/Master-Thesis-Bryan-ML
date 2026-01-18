LIMIT_HOLE = 4
          
def select_valid_lists(indices_list):
    # Check if the list is empty
    if not indices_list:
        return []
    
    # Initiate lists
    valid_lists =[]
    current_group = [indices_list[0]]

    for i in range(1, len(indices_list)):
        current = indices_list[i]
        prev = current_group[-1]

        #  Check the gap
        if (current - prev) <= LIMIT_HOLE: 
            # Gap is within limit: add to current group
            current_group.append(current)
        else :
            # Gap is too big: group is finished.
            if len(current_group)>1:
                valid_lists.append(current_group)
            # Start a new group with the current number
            current_group = [current]
            
    # Handle the last group remaining after the loop
    if len(current_group)> 1 :
        valid_lists.append(current_group)
    return valid_lists

data = [1, 2, 3, 10, 20, 22]
result = select_valid_lists(data)

print(f"Input: {data}")
print(f"Result: {result}")