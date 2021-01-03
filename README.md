# GitHub Guideline

# SmartOMR

# Team Rule

## 노션과 깃허브의 사용

노션은 회의록 작성과 Team Rule, 각 프로그램별 가이드라인을 적어놓는 용도로 한정 그 외 모든건 깃허브에서

- 모든 이슈는(논의, 의견 등) 깃허브에 기록할 것
- Issue별 개인 폴더는 아래 사용법 있음

## Branch 및 Issue에 관하여

### Issue에 관하여

- Issue는 개인별 Issue 목록을 가진다
    - 개인별 Issue는 각자가 개발할 것의 Plan을 계획하고 어느정도 진행했는지 적어놓는것으로 한다.
    - 개인별 Issue에는 서로 Comment는 지양한다.
    - 개인별 Issue는 1주마다 한번씩 새로운 Issue를 생성하여 Refresh한다. ex) Plan by Jaebin W1 / Plan by Jaebin W2
- Master Plan Issue는 각 Repo별 Project의 큰 틀에서의 방향성을 제시한다.
    - Master Plan에는 누구든 질문, 방향성 Comment를 달수 있으며 @를 활용한 Mention을 자주 쓸수있도록 한다.
- 개인별 Issue, Master Plan에 새로운 기능을 추가하거나 큰 변경점이 있다면 새로운 Issue를 등록한다.
    - 본인이 해결하기 까다로운 새로운 Issue 등록시 @Everyone을 통해 모두가 볼수 있도록 한다.
    - Mention에 지정당하면 3일내로 꼭 Comment를 남긴다.
    - Comment주고 받는걸로 안끝나면 회의 Issue에 작성해서 회의 주제로 넘긴다.

### Branch의 경우

- 새로운 기능을 추가할때는 `[제작자]/[기능명]` branch를 만들어 작업한 뒤, 완료 후 PR(Pull Request) 혹은 merge한다.
    - ex) `Jaep/Feature/Index`, `Jaep/Feature/Object_Detection` 등
    - Merge할때는 그냥 하지말고 무조건 Pull Request를 하고 Comment를 받은 후 진행한다.

## Meeting Rule

- 회의가 끝나면 다음 Review Meeting Issue 를 올린다.
- 회의(의견을 묻거나, ~해줬으면 or ~했으면 좋겠다 싶은 거, 진행에 있는 결정 사항 의논 등) 내용이 생길 때마다 Issue에 올려서 대화한다.
    - 이 때 각 주제별로 새로 Issue를 올리고 Review Meeting Issue에 링크를 남긴다.
    - #을 쓰면 알아서 Issue와 PR에 대한 링크를 고를 수 있다.
    - 만약 Issue를 올릴 정도로 복잡하지 않을 것 같다면 Review Meeting Issue에 comment를 남긴다.
- 회의 날짜까지 모든 Issue에 대하여 결론이 지어지면 해당 날짜의 회의는 없어진다.
- 만약 결론이 지어지지 않거나 Comment로 이야기를 나누기 어렵다는 생각이 들 경우 회의날짜에 회의를 진행한다.

## PR Rule

- PR이 올라가고 3일(72시간)안에는 Review를 해준다.