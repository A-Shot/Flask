import os

g=""
path_ = os.listdir("YT")

for i in range(len(path_)):
	path_[i] = os.path.join("YT",path_[i])

print(len(path_))
print(path_)
