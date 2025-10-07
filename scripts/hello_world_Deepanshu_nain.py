
# LANGUAGE: python
# ENV: python3
# AUTHOR: Deepanshu Nain
# GITHUB: https://github.com/Deepanshu-Nain

# it works ;)


msg = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
exec("".join([chr(c) for c in [112,114,105,110,116,40,34] + msg + [34,41]]))
