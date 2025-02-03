from threading import Thread


data = ""


def read_file(file_path, data):
    with open(file_path, "r") as file:
        data += file.read()
        print(data)


sample_txt = Thread(target=read_file, args=("sample3.txt", data))
read_me = Thread(target=read_file, args=("ReadMe.md", data))

sample_txt.start()
read_me.start()

sample_txt.join()
read_me.join()

print(data[45:90])
