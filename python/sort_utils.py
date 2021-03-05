# -*- coding: utf-8 -*-
import collections
import hashlib
import json
import pathlib
import shutil


class SortUtils:
    @classmethod
    def dict_sort(cls, dictory: dict) -> dict:
        """对字典进行排序"""
        ordered_dict = collections.OrderedDict()
        for k in sorted(dictory):
            if isinstance(dictory[k], dict):
                ordered_dict[k] = cls.dict_sort(dictory[k])
            else:
                ordered_dict[k] = dictory[k]
        return ordered_dict

    @classmethod
    def file_md5_sort(cls, path: str, des: str):
        """对文件按照MD5排序，相同的保留一个"""
        md5s = {}
        root = pathlib.Path(path)
        files = root.glob('**/*')
        for file in files:
            with open(file, 'rb') as fobj:
                hlm = hashlib.md5()
                hlm.update(fobj.read())
                md5s[hlm.hexdigest()] = file
        des = pathlib.Path(des)
        for md5 in sorted(md5s):
            shutil.copy(md5s[md5].resolve(), (des / md5s[md5].name).resolve())
        return

    @classmethod
    def json_sort(cls, json_path: str):
        """对json文件进行排序"""
        json_data = None
        with open(json_path, 'r', encoding='UTF-8') as json_file:
            json_data = json.load(json_file)
        with open(json_path, 'w', encoding='UTF-8') as json_file:
            json.dump(cls.dict_sort(json_data), json_file, indent=2)
        return
