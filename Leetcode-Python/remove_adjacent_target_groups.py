def remove_adjacent_target_groups(s: str, target: int) -> str:
    while True:
        stack = []
        i = 0
        changed = False

        while i < len(s):
            j = i 
            while j < len(s) and s[j] == s[i]:
                j += 1
            count = j - i

            if count == target:
                changed = True  # A removal has occurred
            else:
                stack.append(s[i:j])

            i = j

        s = ''.join(stack)
        if not changed:
            break

    return s
    
print(remove_adjacent_target_groups("aaabbcdd", 3))  # Output: "aaac"