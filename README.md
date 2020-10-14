# Project Installation

## 1. Clone The code
```
  git clone https://github.com/javahometech/hire-now
```
## 2. Install serverless plugins

```
  sls plugin install -n serverless-aws-models
  sls plugin install -n serverless-reqvalidator-plugin
  sls plugin install -n serverless-aws-documentation
  sls plugin install -n serverless-iam-roles-per-function
  sls plugin install -n serverless-dynamodb-local
```

## 3. Package the project

```
  sls package
```

## 4. Deploy the project

```
  sls deploy
```
