#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from pymongo import MongoClient


class GithubRepo:
    '一个GithubRepo对应一个Android爬取项目'
    count = 0

    def __init__(self, user="codinguser", repo="gnucash-android"):
        '项目初始化'
        GithubRepo.count += 1

        '初始化基本信息'
        # 用户名
        self.user = user
        # 仓库名
        self.repo = repo
        # GithubRepo名
        self.name = self.user + "_" + self.repo
        # 项目根目录名称
        self.rootdir = "F:/LM/pygithub_learn2.0/pygitthub/" + self.user + "_" + self.repo + "/"

        '初始化数据库名称'
        # mongdbname数据库名称
        self.mongodbname = self.user + "_" + self.repo

        '初始化爬取存储路径'
        ### part1 from  爬取类 Crawling
        self.initcrawlingfilepath()

        '初始化爬取使用的url'
        self.initurl()

        '初始化语料处理文本和模型的存储位置'
        ###part2 from  语料处理类ProcessingCorpus
        self.initprocessingcorpusfilepath()

        '初始化语料处理生成图片的位置'
        self.picpath = os.path.join(self.rootdir, "pic")

        '初始化语料处理存储的数据库'
        self.initmongodbcoll()

    def initcrawlingfilepath(self):
        '初始化爬取类的文件存储路径'
        # 存储 issue 的文件名称与位置
        self.allissuesnumfilename = self.user + "_" + self.repo + "_" + "allissuesnum.txt"
        self.allissuesnumfilepath = os.path.join(self.rootdir, self.allissuesnumfilename)
        # 存储提交的commitsha 的文件名称 与位置
        self.allcommitshafilename = self.user + "_" + self.repo + "_" + "allscommitssha.txt"
        self.allcommitshafilepath = os.path.join(self.rootdir, self.allcommitshafilename)
        # 不同目录，目录不存在则创建
        self.diffdirpath = self.rootdir + "/" + "diff3"
        self.diffdirpath2 = self.rootdir + "/" + "diff2"
        self.diffdirpath3 = self.rootdir + "/" + "diff1"
        if not os.path.exists(self.rootdir):
            os.mkdir(self.rootdir)
        if not os.path.exists(self.diffdirpath):
            os.mkdir(self.diffdirpath)
        if not os.path.exists(self.diffdirpath2):
            os.mkdir(self.diffdirpath2)
        if not os.path.exists(self.diffdirpath3):
            os.mkdir(self.diffdirpath3)

    def initurl(self):
        '初始化爬取所使用的url '
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": "token 744b62ff8eba16ddcff7d89f369f9ab1e1b72dd9",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        self.params = {
            "state": "all"
        }
        self.pacth_headers = {
            "Accept": "application/vnd.github.VERSION.patch",
            "Authorization": "token 744b62ff8eba16ddcff7d89f369f9ab1e1b72dd9",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }

        # https: // api.github.com / repos /codinguser/gnucash-android/issues
        self.issues_url = "https://api.github.com/repos/" + self.user + "/" + self.repo + "/issues"
        self.commits_url = "https://api.github.com/repos/" + self.user + "/" + self.repo + "/commits"

    def initprocessingcorpusfilepath(self):
        '初始化语料处理类的文件存储路径'
        self.difffilename = self.user + "_" + self.repo + "_" + "difftext"
        self.diffpredealfilename = self.user + "_" + self.repo + "_" + "diffpredealtext"
        self.directoryfilename = self.user + "_" + self.repo + "_" + "directory.txt"
        self.diffmodelfilename = self.user + "_" + self.repo + "_" + "diff.model"
        self.difffilepath = os.path.join(self.rootdir, self.difffilename)
        self.diffpredealfilepath = os.path.join(self.rootdir, self.diffpredealfilename)
        self.directoryfilepath = os.path.join(self.rootdir, self.directoryfilename)
        self.diffmodelfilepath = os.path.join(self.rootdir, self.diffmodelfilename)

        self.diffjavafilename = self.user + "_" + self.repo + "_" + "difftext_java"
        self.diffpredealjavafilename = self.user + "_" + self.repo + "_" + "diffpredealtext_java"
        self.directoryjavafilename = self.user + "_" + self.repo + "_" + "directory_java.txt"
        self.diffmodeljavafilename = self.user + "_" + self.repo + "_" + "diff_java.model"
        self.diffjavafilepath = os.path.join(self.rootdir, self.diffjavafilename)
        self.diffpredealjavafilepath = os.path.join(self.rootdir, self.diffpredealjavafilename)
        self.directoryjavafilepath = os.path.join(self.rootdir, self.directoryjavafilename)
        self.diffmodeljavafilepath = os.path.join(self.rootdir, self.diffmodeljavafilename)

        self.diffxmlfilename = self.user + "_" + self.repo + "_" + "difftext_xml"
        self.diffpredealxmlfilename = self.user + "_" + self.repo + "_" + "diffpredealtext_xml"
        self.directoryxmlfilename = self.user + "_" + self.repo + "_" + "directory_xml.txt"
        self.diffmodelxmlfilename = self.user + "_" + self.repo + "_" + "diff_xml.model"
        self.diffxmlfilepath = os.path.join(self.rootdir, self.diffxmlfilename)
        self.diffpredealxmlfilepath = os.path.join(self.rootdir, self.diffpredealxmlfilename)
        self.directoryxmlfilepath = os.path.join(self.rootdir, self.directoryxmlfilename)
        self.diffmodelxmlfilepath = os.path.join(self.rootdir, self.diffmodelxmlfilename)

    def initmongodbcoll(self):
        '初始化语料处理的数据库'
        self.commentsoll = self.openmongdb("comments")
        self.issuescoll = self.openmongdb("issues")
        self.commitscoll = self.openmongdb("commits")
        self.commitsinfocoll = self.openmongdb("commitsinfo")
        self.commentsinfocoll = self.openmongdb("commentsinfo")
        self.issuesinfocoll = self.openmongdb("issuesinfo")
        self.issuesinfo2coll = self.openmongdb("issuesinfo2")
        self.issuesinfo3coll = self.openmongdb("issuesinfo3")
        self.diffinfocoll = self.openmongdb("diffinfo")

    def openmongdb(self, collname='comments'):
        '打开数据库'
        print "打开数据库" + self.mongodbname + ": collname" + collname
        client = MongoClient()
        db = client[self.mongodbname]
        coll = db[collname]
        return coll
