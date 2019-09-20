from collections import defaultdict


r = defaultdict(lambda: defaultdict(set))

r["ami_id1"]["ec2"].add("instance_id1")
r["ami_id1"]["ec2"].add("instance_id2")
r["ami_id1"]["ec2"].add("instance_id1")

r["ami_id1"]["asg"].add("asg1")
r["ami_id1"]["asg"].add("asg2")
r["ami_id1"]["asg"].add("asg3")
r["ami_id1"]["asg"].add("asg3")

print(r)
