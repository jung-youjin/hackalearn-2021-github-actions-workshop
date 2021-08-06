# 🌟 HackaLearn Korea 2021 GitHub Actions Workshop
해카런 코리아 2021 깃헙 액션 워크샵 2021.08.02 8PM KST


<a><img src="https://user-images.githubusercontent.com/37402072/127895635-a7c3d16d-1d04-48bb-8383-0c96db3df6a9.png" width=45%>
<img src="https://user-images.githubusercontent.com/37402072/128051257-7bd066a7-df3b-47aa-bf35-faa4c71c64e6.png" width=45%></a>

<a><img src="https://user-images.githubusercontent.com/37402072/128020028-1cd819f1-7893-4f55-ae79-efa889c957f0.png" width=45%>
<img src="https://user-images.githubusercontent.com/37402072/127895628-1beb43d5-90ce-40a1-8745-684f32eae73b.png" width=45%></a>

## 🚀 Hands-on Demo Contents
### 1. Customize GitHub Actions with Docker 
> Docker를 활용한 커스텀 GitHub Actions 만들기
   - [1.1 Hello Team](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/hello-team)
   - [1.2 Random Joke](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/random-joke)
   - [1.3 Issue Maker](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/issue-maker) 
### 2. Automatize Slack Message with GitHub Actions 
> GitHub Actions를 활용한 자동 Slack Message 전송 Workflow 만들기
   - [2.1 Slack PR Notifier](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/6ed2bb0becc0533b7836c22249d484ca9935839a/.github/workflows/slack-message.yml)
   - [2.2 Slack PR Notifier with GitHub payload](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/workflows/slack-message.yml)

---

### [1.1 Hello Team](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/hello-team)
Uses: ![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
```
/.github
├── actions
│   └── hello-team
|       ├── action.yml
|       ├── main.go
|       └── Dockerfile
└── workflows
    └── hello-team.yml
```


Workflow내 action의 input 값을 Docker env를 통해 GitHub Actions input variable로 받아와 Go main code에서 출력하는 action입니다.

### [1.2 Random Joke](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/random-joke)
Uses: ![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
```
/.github
├── actions
│   └── random-joke
|       ├── action.yml
|       ├── src
|       |   └── main.py
|       ├── requirements.txt
|       └── Dockerfile
└── workflows
    └── random-joke.yml
```

action을 구성하는 python main code에서 외부 API를 호출해 json 값을 반환하여 랜덤하게 배열 값을 골라 출력하는 action입니다.
 또한 GitHub Actions 안에 다른 variable을 output으로 생성하여 다른 action에서 변수 값을 재사용할 수 있도록 구성합니다.

### [1.3 Issue Maker](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/issue-maker) 
Uses: ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
```
/.github
├── actions
│   └── issue-maker
|       ├── action.yml
|       ├── src
|       |   └── index.js
|       ├── package.json
|       └── Dockerfile
└── workflows
    └── make-issue.yml
```

다른 action(1.2 Random Joke Action)에서 받아온 값을 활용해, 그 값을 GitHub Repository 내 Issue 생성으로 markdown 형식으로 반환해 이미지를 포함한 Issue 글을 자동으로 작성합니다.
GitHub Repository를 직접적으로 접근하는 action이기 때문에, `${{ secrets.GITHUB_TOKEN }}` 이 필수적으로 필요합니다.

### [2.1 Slack PR Notifier](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/6ed2bb0becc0533b7836c22249d484ca9935839a/.github/workflows/slack-message.yml)
Uses: ![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![GitHub](https://img.shields.io/badge/github-marketplace-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)
```
/.github
└── workflows
    └── slack-message.yml
```

GitHub 마켓플레이스에 공개된 action을 활용하여, GitHub Repository에 Pull Request가 생성되었을 경우, Slack에 자동으로 메시지를 전송합니다. 
`${{ secrets.SLACK_WEBHOOK_URL }}` 은 slack api 사이트에 접속 후, App 관리를 하는 란에서 Incoming Webhook URL을 활성화하게 되면, Webhook URL이 생성됩니다.
이를 GitHub repository의 Setting > Secrets에 변수로 기입합니다.

### [2.2 Slack PR Notifier with GitHub payload](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/workflows/slack-message.yml)
Uses:  ![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![GitHub](https://img.shields.io/badge/github-marketplace-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)
```
/.github
└── workflows
    └── slack-message.yml
```

GitHub action을 활용하면 생성되는 인자(ex. `${{ github.repository }}`, `${{ github.author }}`)들을 활용해 paylod에 넣어주어 원하는 PR 관련 정보를 담은 Slack 메시지를 전송할 수 있도록 커스터마이징합니다.


**⚠️ 2번 준비 사항**

- Slack Workspace + Channel
- Slack App ([slackapi](https://api.slack.com/apps)) with Incoming Webhook 활성화 
---

![image](https://user-images.githubusercontent.com/37402072/127895635-a7c3d16d-1d04-48bb-8383-0c96db3df6a9.png)

