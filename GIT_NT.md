* `git config --global user.name <user_name>`  : username

* `git config --global user.email <email>`  : email

  * config는 내 로컬과 깃헙 계정을 연결시켜줄 때 1회만!!!! 

  

* `git init` : 레포를 만들고 워킹 디렉토리랑 연결시켜줄때 최초 1회

  * 레포 만들때마다!
  * 여러분들이 레포를 만들때마다 계속 해주셔야한다. 

* `git status` : 워킹 디렉토리에 어떤 변화가 있는지 알아보는 명령어.
  * 워킹 디렉토리 단계와 스테이징 에리아 단계의 변화

* `git add` + `.` : 전체 다 staging area로 올리기

* `git add` + `파일명.확장자` : 이것만 올려
  * ex) `git add 파일1 파일2 파일3`
* `git commit` + `-m` `"commit message"` :
  * 되도록 명령어로 적기
    * 동사형으로 시작하기
    * 영어로 적기
  * 약속일뿐 법은 아니다. 

* `git log --oneline` : `-` (하이픈) 두개입니다. 
  * `commit`된 상황에서 어떤 메시지로 언제 뭐가 올라갔는지 알기위한 명령어
* `git remote add` + `origin <github 주소>` : 내 워킹 디렉토리와 레포지토리 연결
  * `git remote -v` : 리모트가 잘 들어갔는지 확인

* `git push` + `origin master` : 최종으로 깃헙에 올린다!!!

1. `git config --global user.name / email`  잘 적었는지 확인 
2. `git remote 확인` 
   * `git remote add origin <깃헙 주소>`
3. `git add` 했는지
4. `git commit` 잘 했는지 확인



`git branch` : 브랜치의 종류, 어느 브랜치인지 확인하기

`git branch <브랜치>` :  브랜치 생성

* 브랜치 생성 예시`git branch haley`
* 이미 있는 브랜치 명을 작성했을땐 에러 발생

`git checkout <브랜치명>` : 브랜치 이동

* 없는 브랜치 명을 작성했을땐 에러 발생

`git merge <브랜치명>` 

`git clone <레포주소>` : 그대로 복제





## 실습 (30분)

1. `<username>`으로 repository 만들기
   * GIT 폴더 안에도 `<username>` 이름으로 폴더 만들기해야겠죠?
2. `README.md` 를 만들고 `자기소개 페이지 작성하기` 
3. 여러번 반복하기!  `add` - `commit` - `push`

###  5:05

### 5:15



