

x = int(input(" write seconds :"))
m, s = divmod(x, 60)
h, m = divmod(m, 60)
print("{}:{}:{}".format(h, m, s))