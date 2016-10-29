## [Managing Windows Instance Configuration](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-configuration-manage.html)

For more complex automation scenarios, consider using [AWS CloudFormation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/) or [AWS OpsWorks](http://docs.aws.amazon.com/opsworks/latest/userguide/) instead.

First, [SSM Run Command Prerequisites](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/remote-commands-prereq.html)

### Update policies for admins (i.e. 01) to be able to use/run SSM Command
Go to Roles -> Managed Policies -> Attach Policies

1. AmazonEC2RoleforSSM
2. AmazonSSMFullAccess
3. AmazonSSMReadOnlyAccess

See [Delegating Access to SSM Run Command](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/delegate-commands.html)

## Add new Role and Policies for EC2 instances to be managed

1. Add Managed Policies: "RunCommandInstance" (see [Delegating Access to SSM Run Command|http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/delegate-commands.html])
2. Add Role: RunCommandInstance
3. Then attach policies, RunCommandInstance, AmazonEC2RoleforSSM, AmazonSSMFullAccess, AmazonSSMReadOnlyAccess

## Changes to be made to EC2 instances

- All existing VMs did not start with a "managed Role" - need to take an AMI of the instance, and then start the instance again with the Role "RunCommandInstance" (or other name, such that we can add policies for remote managing the instances later easily)
- Need to update with the latest version of EC2Config Service on Windows

## Prepare and run SSM Documents (from console or awscli)

see Document [examples](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-configuration-manage.html)

From console

1. EC2 -> Commands -> Documents -> Create Document
2. EC2 -> Commands -> Command History -> Run a command

Or from awscli (se attached):

1. create a json file containing the command
2.  aws ssm create-document --profile gf --content file://ssm-ec2-config.json --name "ssm-ec2-cyberduck-config-v1" 
3. aws ssm create-association --profile gf --instance-id i-09cc28d8 --name "ssm-ec2-cyberduck-config-v1"

** Using SSM, only can install msi, not setup.exe
