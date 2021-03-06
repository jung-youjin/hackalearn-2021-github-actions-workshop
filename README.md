# ๐ HackaLearn Korea 2021 GitHub Actions Workshop
ํด์นด๋ฐ ์ฝ๋ฆฌ์ 2021 ๊นํ ์ก์ ์ํฌ์ต 2021.08.02 8PM KST


<a><img src="https://user-images.githubusercontent.com/37402072/127895635-a7c3d16d-1d04-48bb-8383-0c96db3df6a9.png" width=45%>
<img src="https://user-images.githubusercontent.com/37402072/128051257-7bd066a7-df3b-47aa-bf35-faa4c71c64e6.png" width=45%></a>

<a><img src="https://user-images.githubusercontent.com/37402072/128020028-1cd819f1-7893-4f55-ae79-efa889c957f0.png" width=45%>
<img src="https://user-images.githubusercontent.com/37402072/127895628-1beb43d5-90ce-40a1-8745-684f32eae73b.png" width=45%></a>

## ๐ Hands-on Demo Contents
### 1. Customize GitHub Actions with Docker 
> Docker๋ฅผ ํ์ฉํ ์ปค์คํ GitHub Actions ๋ง๋ค๊ธฐ
   - [1.1 Hello Team](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/hello-team)
   - [1.2 Random Joke](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/random-joke)
   - [1.3 Issue Maker](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/issue-maker) 
### 2. Automatize Slack Message with GitHub Actions 
> GitHub Actions๋ฅผ ํ์ฉํ ์๋ Slack Message ์ ์ก Workflow ๋ง๋ค๊ธฐ
   - [2.1 Slack PR Notifier](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/6ed2bb0becc0533b7836c22249d484ca9935839a/.github/workflows/slack-message.yml)
   - [2.2 Slack PR Notifier with GitHub payload](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/workflows/slack-message.yml)

---

### [1.1 Hello Team](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/hello-team)
Uses: ![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
```
/.github
โโโ actions
โ   โโโ hello-team
|       โโโ action.yml
|       โโโ main.go
|       โโโ Dockerfile
โโโ workflows
    โโโ hello-team.yml
```


Workflow๋ด action์ input ๊ฐ์ Docker env๋ฅผ ํตํด GitHub Actions input variable๋ก ๋ฐ์์ Go main code์์ ์ถ๋ ฅํ๋ action์๋๋ค.

### [1.2 Random Joke](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/random-joke)
Uses: ![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
```
/.github
โโโ actions
โ   โโโ random-joke
|       โโโ action.yml
|       โโโ src
|       |   โโโ main.py
|       โโโ requirements.txt
|       โโโ Dockerfile
โโโ workflows
    โโโ random-joke.yml
```

action์ ๊ตฌ์ฑํ๋ python main code์์ ์ธ๋ถ API๋ฅผ ํธ์ถํด json ๊ฐ์ ๋ฐํํ์ฌ ๋๋คํ๊ฒ ๋ฐฐ์ด ๊ฐ์ ๊ณจ๋ผ ์ถ๋ ฅํ๋ action์๋๋ค.
 ๋ํ GitHub Actions ์์ ๋ค๋ฅธ variable์ output์ผ๋ก ์์ฑํ์ฌ ๋ค๋ฅธ action์์ ๋ณ์ ๊ฐ์ ์ฌ์ฌ์ฉํ  ์ ์๋๋ก ๊ตฌ์ฑํฉ๋๋ค.

### [1.3 Issue Maker](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/actions/issue-maker) 
Uses: ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
```
/.github
โโโ actions
โ   โโโ issue-maker
|       โโโ action.yml
|       โโโ src
|       |   โโโ index.js
|       โโโ package.json
|       โโโ Dockerfile
โโโ workflows
    โโโ make-issue.yml
```

๋ค๋ฅธ action(1.2 Random Joke Action)์์ ๋ฐ์์จ ๊ฐ์ ํ์ฉํด, ๊ทธ ๊ฐ์ GitHub Repository ๋ด Issue ์์ฑ์ผ๋ก markdown ํ์์ผ๋ก ๋ฐํํด ์ด๋ฏธ์ง๋ฅผ ํฌํจํ Issue ๊ธ์ ์๋์ผ๋ก ์์ฑํฉ๋๋ค.
GitHub Repository๋ฅผ ์ง์ ์ ์ผ๋ก ์ ๊ทผํ๋ action์ด๊ธฐ ๋๋ฌธ์, `${{ secrets.GITHUB_TOKEN }}` ์ด ํ์์ ์ผ๋ก ํ์ํฉ๋๋ค.

### [2.1 Slack PR Notifier](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/6ed2bb0becc0533b7836c22249d484ca9935839a/.github/workflows/slack-message.yml)
Uses: ![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![GitHub](https://img.shields.io/badge/github-marketplace-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)
```
/.github
โโโ workflows
    โโโ slack-message.yml
```

GitHub ๋ง์ผํ๋ ์ด์ค์ ๊ณต๊ฐ๋ action์ ํ์ฉํ์ฌ, GitHub Repository์ Pull Request๊ฐ ์์ฑ๋์์ ๊ฒฝ์ฐ, Slack์ ์๋์ผ๋ก ๋ฉ์์ง๋ฅผ ์ ์กํฉ๋๋ค. 
`${{ secrets.SLACK_WEBHOOK_URL }}` ์ slack api ์ฌ์ดํธ์ ์ ์ ํ, App ๊ด๋ฆฌ๋ฅผ ํ๋ ๋์์ Incoming Webhook URL์ ํ์ฑํํ๊ฒ ๋๋ฉด, Webhook URL์ด ์์ฑ๋ฉ๋๋ค.
์ด๋ฅผ GitHub repository์ Setting > Secrets์ ๋ณ์๋ก ๊ธฐ์ํฉ๋๋ค.

### [2.2 Slack PR Notifier with GitHub payload](https://github.com/jung-youjin/hackalearn-2021-github-actions-workshop/blob/main/.github/workflows/slack-message.yml)
Uses:  ![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![GitHub](https://img.shields.io/badge/github-marketplace-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)
```
/.github
โโโ workflows
    โโโ slack-message.yml
```

GitHub action์ ํ์ฉํ๋ฉด ์์ฑ๋๋ ์ธ์(ex. `${{ github.repository }}`, `${{ github.author }}`)๋ค์ ํ์ฉํด paylod์ ๋ฃ์ด์ฃผ์ด ์ํ๋ PR ๊ด๋ จ ์ ๋ณด๋ฅผ ๋ด์ Slack ๋ฉ์์ง๋ฅผ ์ ์กํ  ์ ์๋๋ก ์ปค์คํฐ๋ง์ด์งํฉ๋๋ค.


**โ ๏ธ 2๋ฒ ์ค๋น ์ฌํญ**

- Slack Workspace + Channel
- Slack App ([slackapi](https://api.slack.com/apps)) with Incoming Webhook ํ์ฑํ 
---

![image](https://user-images.githubusercontent.com/37402072/127895635-a7c3d16d-1d04-48bb-8383-0c96db3df6a9.png)

