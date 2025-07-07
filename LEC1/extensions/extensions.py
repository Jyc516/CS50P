def main():
    file = input("File name: ").strip().lower()
    length = len(file)
    types = [
        {"media type": "image", "file type": "gif", "suffix": "gif"},
        {"media type": "image", "file type": "jpeg", "suffix": "jpg"},
        {"media type": "image", "file type": "png", "suffix": "png"},
        {"media type": "application", "file type": "pdf", "suffix": "pdf"},
        {"media type": "text", "file type": "plain", "suffix": "txt"},
        {"media type": "application", "file type": "zip", "suffix": "zip"},
        {"media type": "image", "file type": "jpeg", "suffix": "jpeg"},
        {"media type": "application", "file type": "octet-stream", "suffix": None},
    ]
    if file[length - 4] == ".":
        for i in range(6):
            if check_suffix(file, length, types[i]["suffix"], len(types[i]["suffix"])):
                print(types[i]["media type"], types[i]["file type"], sep = "/")
                return
        print(types[7]["media type"], types[7]["file type"], sep = "/")
    elif file[length - 5] == "." and check_suffix(file, length, types[6]["suffix"], len(types[6]["suffix"])):
        print(types[6]["media type"], types[6]["file type"], sep = "/")
    else:
        print(types[7]["media type"], types[7]["file type"], sep = "/")


def check_suffix(string, length_str, suffix, length_suf):
    for _ in range(length_suf):
        if string[length_str - length_suf + _] != suffix[_]:
            return False
    return True


main()
