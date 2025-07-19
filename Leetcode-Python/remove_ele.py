def remove_element(numslist_, num):
    i = 0
    
    while i < len(numslist_):
        if numslist_[i] == num:
            numslist_.remove(num)
        else:
            i += 1
    return numslist_, len(numslist_)
        
        



nums1 = [1, 1, 1, 1, 1]
val1 = 1

print(nums1)
print(remove_element(numslist_=nums1, num=val1))