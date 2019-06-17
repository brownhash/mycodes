import time
import subprocess

def ports():
    def epoch_to_readable(epoch):
        readable=time.strftime("%d/%m/%y - %H:%M:%S",epoch)
        return(readable)

    def timestamp():
        time_s=epoch_to_readable(time.localtime())
        return (time_s)

    def port_status():
        cmd_out = subprocess.Popen(['netstat','-ap','tcp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()

        writer = open("cmd.txt", "a")
        string_to_write = "\n" + "-------------------------" + "\n" + str(timestamp()) + "\n" + "-------------------------"+"\n"
        writer.write(string_to_write)
        writer.close()

        writer = open("cmd.txt", "a")
        writer.write(cmd_out[0])
        writer.close()
