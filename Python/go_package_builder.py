import os

binary_name = "my_binary"
version_data = {
    "darwin" : ["386", "amd64", "arm", "arm64"],
    "dragonfly" : ["amd64"],
    "freebsd" :	["386", "amd64", "arm"],
    "linux" : ["386", "amd64", "arm", "arm64", "ppc64", "ppc64le", "mips", "mipsle", "mips64", "mips64le"],
    "netbsd" : ["386", "amd64", "arm"],
    "openbsd" : ["386", "amd64", "arm"],
    "solaris" : ["amd64"],
}

for os_name in version_data:
    architecture_list = version_data[os_name]
    for arch in architecture_list:
        filename = "{}/{}".format(os_name+"-"+arch, binary_name)
        build_command = "env GOOS={} GOARCH={} go build -o {} *.go".format(os_name, arch, filename)

        os.system(build_command)