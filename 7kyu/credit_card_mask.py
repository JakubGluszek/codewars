# return masked string
def maskify(cc: str):
    return cc if len(cc) < 4 else "".join(["#" for _ in cc[:-4]]) + cc[len(cc) - 4 :]
