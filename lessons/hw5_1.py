#
# st='Nice to meet you'
# def reverse(st):
#     return  " ".join(reversed(st.split())).strip()
#     # return " ".join(reversed(st.split())).strip()
# print(reverse(st))

# l = ['Vita', 'Serhii', 'Maria']
# def reverse_list(l):
#     return list(reversed(l))
# print(reverse_list(l))

def correct_tail(body, tail):
    sub = tail.length
    sub = body.substr(len(body) - len(tail.length))
    print(sub)
    if sub == tail:
        return True
    else:
        return False