import datetime
import mimetypes

def get_ext(mime):
    if mime == "text/plain":
        return ".txt"
    return mimetypes.guess_extension(mime);

def gen_filename(u, f):
    return u+"-"+str(datetime.datetime.now().timestamp()).split(".")[0]+get_ext(f.content_type)
