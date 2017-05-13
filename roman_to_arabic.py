# convert roman to arabic

digits = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def convert(num):
    res = 0
    for i in range(len(num)):
        # if the first digits is less that the next, we subtract it
        # that way we dont need to skip anything
        if i != len(num)-1 and digits[num[i]] < digits[num[i+1]]:
            res -= digits[num[i]]
        else:
            res += digits[num[i]]

    return res
