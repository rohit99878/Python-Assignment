"""Write a function that takes a list of strings and returns the longest common
 prefix among them."""
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Test case
print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
