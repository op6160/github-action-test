import os

def main():
    result_dir = "../result/push_test/"
    result_file_name = "test_result"
    result_count = 0
    result_file_extension = ".txt"

    if not os.path.exists(result_dir):
        os.mkdir("../result")
        os.mkdir(result_dir)

    while 1:
        result_file_path = result_dir+result_file_name+str(result_count)+result_file_extension
        if not os.path.exists(result_file_path):
            with open(result_file_path, "w") as file:
                file.write(str(result_count))
                print(f"file writing done: {result_file_path}")
            if os.path.exists(result_file_path):                
                return result_count
            else:
                raise FileExistsError(result_file_path)
        result_count += 1

if __name__ == "__main__":
    main()