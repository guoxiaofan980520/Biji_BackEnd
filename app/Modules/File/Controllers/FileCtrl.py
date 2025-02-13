from app.Database.FileDAO import FileDAO
from app.Database.ShareCodeDAO import ShareCodeDAO
from app.Modules.Log.Controllers import LogCtrl

from app.Modules.File.Models.File import File
from app.Modules.File.Exceptions.FileNotExistError import FileNotExistError
from app.Modules.File.Exceptions.InsertError import InsertError
from app.Modules.File.Exceptions.DeleteError import DeleteError
from app.Modules.File.Exceptions.FileUploadError import FileUploadError

import json
import os

from app.Utils.Exceptions.BodyRawJsonError import BodyRawJsonError


def getAllFiles(username: str, foldername: str) -> [File]:
    '''
    查询所有文件
    '''
    fileDao = FileDAO()
    return fileDao.queryFiles(username, foldername)

def getAllFilesByUsername(username: str) -> [File]:
    '''
    查询所有文件
    '''
    fileDao = FileDAO()
    return fileDao.queryFilesByUsername(username)

def getOneFile(username: str, foldername: str, filename: str, id: int) -> File:
    '''
    查询一个文件
    '''
    fileDao = FileDAO()
    ret = fileDao.queryOneFile(username, foldername, filename, id)
    if ret == None:
        raise FileNotExistError(filename)
    return ret


def insertFile(username: str, file: File) -> bool:
    '''
    插入一个文件
    '''
    fileDao = FileDAO()
    if fileDao.insertFile(file):
        LogCtrl.updateFileLog(username)
        return True
    else:
        raise InsertError(file.filename)

def deleteFile(username: str, file: File) -> bool:
    '''
    删除一个文件
    '''
    fileDao = FileDAO()
    if fileDao.deleteFile(file):
        LogCtrl.updateFileLog(username)
        return True
    else:
        raise DeleteError(file.filename)

def deleteFileByClass(username: str, fileClassName: str) -> bool:
    '''
    删除一类文件
    '''
    fileDao = FileDAO()
    if fileDao.deleteFileByClass(username, fileClassName):
        LogCtrl.updateFileLog(username)
        return True
    else:
        raise DeleteError(fileClassName, False)

def getDocumentsFromReqData(username: str, reqdata: str) -> [File]:

    try:
        postjsons = json.loads(reqdata)

        ret = []
        for postjson in postjsons:
            ret.append(checkJson(username, json.loads(postjson)))

    except:
        # 解析错误
        raise BodyRawJsonError()

    return ret

def checkJson(username: str, postjson) -> File:
    '''
    检查 Json 并转化
    '''
    keys = ['id', 'foldername', 'filename']
    nonePostKeys = [
        key for key in keys
        if key not in postjson or postjson[key] == None
    ]
    if not len(nonePostKeys) == 0:
        # 缺少参数
        raise(BodyRawJsonError(nonePostKeys))

    if not len(postjson) == len(keys):
        # 参数过多
        raise BodyRawJsonError()

    try:
        return File(username, postjson['id'], postjson['foldername'], postjson['filename'], '')
    except:
        # 内容错误
        raise BodyRawJsonError()

def saveFile(file, username: str):
    '''
    保存用户文件
    '''
    if file:
        filepath = './usr/file/{}/'.format(username)  # 存放文件夹
        if not os.path.exists(filepath):
            os.makedirs(filepath)

        filepath = os.path.join(filepath, file.filename)  # 最终路径
        file.save(filepath)
        if os.path.exists(filepath):
            return (file.filename, filepath)
        else:
            raise FileUploadError(file.filename)
    else:
        raise FileUploadError()


def getFile(username: str, filename: str):
    '''
    获得用户文件
    '''
    filepath = './usr/file/{}/'.format(username)
    filepath = os.path.join(filepath, filename)

    if not os.path.exists(filepath):
        raise FileNotExistError(filename)

    with open(filepath, 'rb') as f:
        return f


def pushFile(username: str, files: [File]) -> bool:
    '''
    同步文件
    '''
    fileDao = FileDAO()
    r = False

    for file in files:
        if fileDao.queryOneFile(username, file.foldername, file.filename, file.id) is None:
            r = insertFile(username, file)

    return r

def addShareCode(usr: str, folder: str) -> bool:
    '''
    存储share code
    '''
    shareCodeDao = ShareCodeDAO()
    return shareCodeDao.addShareCode(usr, folder)

def checkShareCode(usr: str, folder: str) -> bool:
    '''
    检查share code
    '''
    shareCodeDao = ShareCodeDAO()
    return shareCodeDao.checkShareCode(usr, folder)