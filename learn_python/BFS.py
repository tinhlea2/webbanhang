def read_file(file_path):
    f=open(file_path)
    lines=f.readline()
    print ('Nội dung dòng đầu: ', (lines))
    lines=[line.strip() for line in lines]
    data=[]
    for line in lines:
        data.append([int(num) for num in line.strip(' ')])
    
    return data


if __name__ =="__main__":
    data=read_file('D:\\wordspace\\learn_python\\bfs.txt')
    print(data)