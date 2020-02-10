# AWS Serverless CI/CD
AWSでサーバレスのCI/CD環境を作成するサンプルプロジェクト

## 構成
- Python3.7
- Serverless Framework
- CodeCommit
- CodePipeline
- CodeBuild

## CI/CDスタックの作成
```
aws cloudformation create-stack --stack-name sample-service --template-body file://cf/cicd.yml --capabilities CAPABILITY_NAMED_IAM
```
