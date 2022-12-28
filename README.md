# Project_Zomboid_MOD_Crawler

프로젝트 좀보이드 모드 모음집 링크를 통하여 자동으로 MOD ID, MAP NAME, MOD NAME, MAP FOLDER를 수집합니다.

# 사용방법

0. !pip install bs4 로 beautifulsoup을 설치합니다.

1. 좀보이드 모드를 모아둔 모음집을 Public으로 만듭니다.

2. 좀보이드 모드 모음집의 ID를 가져와 입력해줍니다.

3. 크롤링 후 .ini파일에 넣어야할 값을 보여줍니다.

# TODO

1. 가상환경 자동 생성 후 requirements.txt로 자동으로 설치되어서 실행까지 마칠 수 있도록

2. 주피터 노트북이 아닌 쉘 혹은 배치파일로 자동으로 모든 작업을 끝낼 수 있도록

3. DockerCompose로 사용할 수 있게 .env 파일로 출력할 수 있도록

4. 최종목표는 DockerFile을 만드는 것이지만 3번까지만 해도 만족할듯

# Reference

사용된 도커 이미지: https://hub.docker.com/r/renegademaster/zomboid-dedicated-server
