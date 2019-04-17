# aws-ec2-controlly

Acloud Guru example on using boto3

## About

This project is a demo from the acloud guru python course and uses boto3

## Configuring

controlly uses the configuration file created by the AWS Cli. e.g
`aws configure --profile default`

using pipenv
`pipenv install`

## Running

```bash
$ pipenv run "python controlly/controlly.py <command> <subcommand> <--project=PROJECT>"
```

**command** is instances, volume, or snapshots
**subcommand** - depends on command
**project** is optional
