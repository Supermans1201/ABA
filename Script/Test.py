#!/usr/bin/python
# -*- coding: UTF-8 -*-
from GetInformation.GithubRepo import GithubRepo
from GetInformation.CrawlGithub import CrawlGithub
import os
if __name__=="__main__":
    # 初始化Github仓库
    repo= GithubRepo("owncloud","android")
    repo.printInfo()
    # 初始化爬取类
    crawl=CrawlGithub(repo)
    # 1
    crawl.gen_all_issues_num_txt()
    crawl.gen_all_commits_sha_txt()