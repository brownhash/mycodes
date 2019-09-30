import os
import stat


def file_size(filepath):
    try:
        size = os.lstat(filepath)[stat.ST_SIZE] / 1024
        unit = "KiB"

        if size > 1024 + (1024 / 2):
            unit = "MB"
            size = size / 1024

        if unit == "MB" and size > 1024 + (1024 / 2):
            unit = "GiB"
            size = size / 1024

        return {'size': round(size, 2), 'unit': unit}
    except FileNotFoundError:
        return "File not found!"


def i_node_num(filepath):
    try:
        i_node = os.lstat(filepath)[stat.ST_INO]
        return i_node
    except FileNotFoundError:
        return "File not found!"


def time_info(filepath):
    try:
        a_time = os.lstat(filepath)[stat.ST_ATIME]
        m_time = os.lstat(filepath)[stat.ST_MTIME]
        c_time = os.lstat(filepath)[stat.ST_CTIME]
        time_data = {'access_time': a_time, 'modification_time': m_time, 'status_change_time': c_time}
        return time_data
    except FileNotFoundError:
        return "File not found!"


def file_data(filepath):
    size = file_size(filepath)
    i_node = i_node_num(filepath)
    time_data = time_info(filepath)
    data = {'inode': i_node, 'size_data': size, 'time_data': time_data}

    return data


file_path = "/Users/harshit.sharma/Downloads/Avengers Endgame 2019 HDTC " \
           "Dual Audio Hindi English 720p AAC - mkvCinemas [Telly].mkv"
print(file_data(file_path))
