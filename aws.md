# AWS

```
################################################################################
# AWS Command Line shell
pip install aws-shell

################################################################################
# Resize EBS of a Ubuntu
sudo growpart /dev/xvda 1
sudo resize2fs /dev/xvda1

################################################################################
# Docker ECR
aws ecr get-login --no-include-email | bash

################################################################################
# Elastic Beanstalk, quick local packaging

docker build -t local/my_app .
docker run -d -p 8080:8080 local/my_app:latest
zip -r app.zip my_app env setup.py *.ini Dockerfile Dockerrun.aws.json constraints.txt MANIFEST.in

aws elasticbeanstalk list-available-solution-stacks

################################################################################
# Rename user
aws iam update-user --user-name devpos --new-user-name devops --profile my_profile

################################################################################
# Find IP in security group
aws ec2 describe-security-groups --profile networks --filters Name=ip-permission.from-port,Values=22 Name=ip-permission.cidr,Values='203.87.3.106/32' Name=ip-permission.cidr,Values='61.61.61.61/32' --query SecurityGroups[*].{groupId:GroupId}

################################################################################
# Get latest ECS Optimized AMI
latest_ami=`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/recommended/image_id --region ap-southeast-2 --query "Parameters[0].Value" | awk -F \" '{print $2}'`
echo $latest_ami

################################################################################
# Using aws ssm (simple systems manager)

aws ssm list-documents
aws ssm create-document --content file://ssm-ec2-config.json --name "ssm-ec2-cyberduck-config-v1" 
aws ssm create-association --instance-id <instance_id> --name "ssm-ec2-cyberduck-config-v1"
aws ssm delete-document --name "ssm-ec2-cyberduck-config-v1"

```