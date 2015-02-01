名詞
----
- image
- container

指令
----
- 觀看 docker 的版本

  - docker version

- 用關鍵字搜尋 docker image

  - docker search <KEYWORD>

- 下載指定的 image

  - docker pull <USERNAME>/<IMAGE_NAME>

- 列出現有的 image

  - docker image 

- 在該 image 內執行程式 (以該 image 為基礎開啟一個 container?)

  - docker run <IMAGE_NAME> <COMMAND>

  - docker run <IMAGE_NAME> apt-get install ...

    - use package management system in docker

- 列出 container 及其 id

  - docker ps
  - docker ps -l

- 更新 repo?

  - docker commit <CONTAINER_ID> <REPO>

概念
----
- daemon?
- 前端1: container + version control
- dockerhub: docker 版的 github, 有 version control 的功能後有這個也不意外.
- 後端1: pid 的 namespace 機制, container 跟外部 OS 的 pid 獨立. (process id)

reference
---------
- `Docker official website 10 mins tutorial - try it <https://www.docker.com/tryit/>`_
- `門外漢的 Docker 小試身手 <http://www.codedata.com.tw/social-coding/docker-layman-abc/>`_
- `docker 原理簡介 <http://blog.blackwhite.tw/2013/12/docker.html>`_
- `Introduction to Docker (這篇比較偏向 docker 的使用方式) <http://hungmingwu-blog.logdown.com/posts/196996-introduction-to-docker>`_

- `Docker Getting Start: Related Knowledge <http://tiewei.github.io/cloud/Docker-Getting-Start/>`_
- `小心暗藏惡意軟件：淺談 Docker 安全性 <http://www.hkitblog.com/?p=22552>`_
- `Docker 中文指南 <http://www.widuu.com/chinese_docker/>`_
