def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword..................{}".format(k))
    print("var-keyword..............{}".format(kwargs))


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8, random_var_name=8.5)

# p1 1 and 2
# p2 3, 4, 5, 9
# *args
# k is 6, 7, 8
# **kwargs all of them