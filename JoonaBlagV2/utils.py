from time import strftime

def gen_dirname(instance, filename):
    print(instance, filename)
    return "uploads/{}/{}/{}".format(instance.author, strftime("%Y/%m/%d"), filename)
