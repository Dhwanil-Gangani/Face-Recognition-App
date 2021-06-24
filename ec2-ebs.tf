provider "aws" {
  
  region = "ap-south-1"
  profile = "default"

}

resource "aws_instance" "ostask6" {  
  ami = "ami-010aff33ed5991201"
  instance_type = "t2.micro"
  
  tags = {
    Name = "Task-6 OS"
  }    
}


resource "aws_ebs_volume" "vol" {
  availability_zone = aws_instance.ostask6.availability_zone
  size              = 5

  tags = {
    Name = "Tast-6 Volume"
  }
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.vol.id
  instance_id = aws_instance.ostask6.id
}

