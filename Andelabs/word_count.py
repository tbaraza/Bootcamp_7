def words(string):
    """
    The function counts the word occurence in a string
        e.g. For "olly olly in come free"

            olly: 2
            in: 1
            come: 1
            free: 1
    """
    new_list = string.split()
    string_dict = {}

    for word in new_list:
        if word.isdigit(): 
            word = int(word)

        if word in string_dict:
            string_dict[word] = string_dict[word] + 1

        else:
            string_dict[word] = 1
      return string_dict

print words("Hi hi hi higher car carpet how are : : yah")
 

Click here to type a chat message. Supports GitHub flavoured markdown.



def find_max_min(A):
    max_, min_ = A[0], A[0]
    a = []
    for i in A:
        if i > max_:
            max_ = i

        if i < min_:
            min_ = i

    if max_ != min_:
    	a.append(max_)
    	a.append(min_)

    if max_ == min_:
    	a.append(len(A))

    return a
  

print find_max_min([2, 4, 6, 8, 78, 90])
print find_max_min([4, 6])
print find_max_min([1, 1, 1])
