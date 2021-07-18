#xylophone


## YOLO Photo Album

YOLOv5 object detection을 활용한 포토 앨범 만들기

- 갤러리 뷰 사용

![](result.png)

## Run

```
python3 manage.py migrate
python3 manage.py runserver 
```

- 로컬 접속시 http://127.0.0.1:8000/

---
API url

|url|method|설명|
|:---|---:|:---|
|/|get|갤러리페이지|
|/photo/|get|사진 리스트|
|/photo/|post|파일 업로드|
|/photo/{id}/|get|사진 상세페이지|
---



## TODO
- ~~init db 만들기~~
- ~~사진 정보를 데이터베이스에 저장한다. (sqlLite 사용)~~
- ~~사용자가 파일 업로드를 할 수 있어야 한다~~
- ~~업로드한 파일을 yolo를 적용시켜 정보를 디비에 저장해야 한다.~~
- ~~업로드한 파일들을 볼 수 있어야 한다. (list)~~
- ~~업로드한 파일에 대한 detection 라벨링 보여주기~~
- 파일명에 한글, 띄어쓰기가 있다면 에러가 발생한다
- ~~모든 페이지에서 index로 가는 링크 추가~~  
- ~~/album/index 페이지를 / 로 변경하기 (url 변경하기)~~ 
- ~~index 페이지에 /album/photo/ 갈수 있는 링크 or 버튼 추가하기~~
- 데이터에 쓰일 사진 구하기 
- (옵션) 업로드한 파일에 대한 리사이징 작업
- ~~(옵션) 업로드한 파일이 어느 카테고리에 속하는지 미리 보여주기 화면~~
- ~~(옵션) 갤러리 수정 - 여러개가 아닌 분류 하나씩 보도록, 더 심플한 갤러리로 변경~~
- (옵션) 태그에 더 큰 분류를 추가 한다.(동물 : 개+고양이+곰 을 포함한다 / 자연 : 동물+식물을 포함한다)
- ~~(옵션) 식물, fish에 대한 데이터 셋을 추가한다.~~
- (옵션) 같은 이름에 대한 처리 (현재는 덮어쓴다.)
- (옵션) 로깅
- ~~(옵션) flask -> django~~

  
## Dependency

- Python 3
- torch==1.9.0
- torchvision==0.10.0
- Django==3.2.5


## Reference

- YOLOv5 https://github.com/ultralytics/yolov5
- isotope https://isotope.metafizzy.co/
