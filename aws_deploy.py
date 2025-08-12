#!/usr/bin/env python3
"""
AWS Deployment Script for Skerritt Economics
Handles deployment to AWS Lightsail or EC2
"""

import os
import sys
import json
import subprocess
import argparse
from datetime import datetime

class AWSDeployer:
    def __init__(self, instance_name=None, instance_ip=None):
        self.instance_name = instance_name
        self.instance_ip = instance_ip
        self.ssh_key_path = os.path.expanduser("~/.ssh/LightsailDefaultKey-us-east-1.pem")
        self.remote_user = "ubuntu"
        self.remote_path = "/opt/skerritt-economics"
        
    def check_aws_cli(self):
        """Verify AWS CLI is installed and configured"""
        try:
            result = subprocess.run(["aws", "--version"], capture_output=True, text=True)
            print(f"✅ AWS CLI found: {result.stdout.strip()}")
            
            # Check configuration
            result = subprocess.run(["aws", "configure", "get", "region"], capture_output=True, text=True)
            if result.returncode != 0:
                print("❌ AWS CLI not configured. Please run: aws configure")
                return False
            
            print(f"✅ AWS Region: {result.stdout.strip()}")
            return True
        except FileNotFoundError:
            print("❌ AWS CLI not found. Please install it first.")
            return False
    
    def get_lightsail_instances(self):
        """Get list of Lightsail instances"""
        try:
            result = subprocess.run(
                ["aws", "lightsail", "get-instances"],
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print(f"Error getting instances: {result.stderr}")
                return []
            
            data = json.loads(result.stdout)
            instances = []
            
            for instance in data.get('instances', []):
                instances.append({
                    'name': instance['name'],
                    'state': instance['state']['name'],
                    'ip': instance.get('publicIpAddress', 'N/A'),
                    'location': instance['location']['regionName'],
                    'blueprint': instance['blueprintName']
                })
            
            return instances
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def select_instance(self):
        """Let user select an instance or provide IP"""
        instances = self.get_lightsail_instances()
        
        if not instances:
            print("No Lightsail instances found.")
            ip = input("Enter instance IP address manually: ").strip()
            if ip:
                self.instance_ip = ip
                return True
            return False
        
        print("\n📊 Available Lightsail Instances:")
        print("-" * 60)
        for i, inst in enumerate(instances, 1):
            status = "🟢" if inst['state'] == 'running' else "🔴"
            print(f"{i}. {status} {inst['name']}")
            print(f"   IP: {inst['ip']}")
            print(f"   Location: {inst['location']}")
            print(f"   Blueprint: {inst['blueprint']}")
        
        choice = input("\nSelect instance number (or enter IP address): ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(instances):
            selected = instances[int(choice) - 1]
            self.instance_name = selected['name']
            self.instance_ip = selected['ip']
            print(f"\n✅ Selected: {self.instance_name} ({self.instance_ip})")
            return True
        elif '.' in choice:  # Assume it's an IP address
            self.instance_ip = choice
            return True
        
        print("Invalid selection")
        return False
    
    def test_ssh_connection(self):
        """Test SSH connection to instance"""
        print(f"\n🔐 Testing SSH connection to {self.instance_ip}...")
        
        # Check if SSH key exists
        if not os.path.exists(self.ssh_key_path):
            print(f"⚠️  SSH key not found at {self.ssh_key_path}")
            self.ssh_key_path = input("Enter path to SSH key: ").strip()
            if not os.path.exists(self.ssh_key_path):
                print("❌ SSH key file not found")
                return False
        
        # Set correct permissions
        os.chmod(self.ssh_key_path, 0o400)
        
        # Test connection
        cmd = [
            "ssh", "-i", self.ssh_key_path,
            "-o", "StrictHostKeyChecking=no",
            "-o", "ConnectTimeout=10",
            f"{self.remote_user}@{self.instance_ip}",
            "echo 'Connection successful'"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ SSH connection successful")
            return True
        else:
            print(f"❌ SSH connection failed: {result.stderr}")
            return False
    
    def deploy_with_docker(self):
        """Deploy using Docker"""
        print("\n🐳 Deploying with Docker...")
        
        # Commands to run on remote
        commands = [
            f"cd {self.remote_path}",
            "git pull origin main",
            "docker-compose down",
            "docker-compose build --no-cache",
            "docker-compose up -d",
            "docker-compose ps"
        ]
        
        for cmd in commands:
            print(f"  Running: {cmd}")
            ssh_cmd = [
                "ssh", "-i", self.ssh_key_path,
                f"{self.remote_user}@{self.instance_ip}",
                cmd
            ]
            result = subprocess.run(ssh_cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"  ⚠️  Warning: {result.stderr}")
            else:
                print(f"  ✅ {result.stdout[:100]}")
    
    def deploy_with_git(self):
        """Deploy using Git pull and restart"""
        print("\n📦 Deploying with Git...")
        
        commands = [
            f"cd {self.remote_path}",
            "git pull origin main",
            "source venv/bin/activate && pip install -r requirements.txt",
            "source venv/bin/activate && python manage.py migrate",
            "source venv/bin/activate && python manage.py collectstatic --noinput",
            "sudo systemctl restart gunicorn",
            "sudo systemctl restart nginx",
            "sudo systemctl status gunicorn --no-pager"
        ]
        
        for cmd in commands:
            print(f"  Running: {cmd}")
            ssh_cmd = [
                "ssh", "-i", self.ssh_key_path,
                f"{self.remote_user}@{self.instance_ip}",
                f"bash -c '{cmd}'"
            ]
            result = subprocess.run(ssh_cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"  ⚠️  Warning: {result.stderr}")
            else:
                print(f"  ✅ Success")
    
    def backup_database(self):
        """Backup remote database before deployment"""
        print("\n💾 Backing up database...")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"backup_{timestamp}.sql"
        
        cmd = [
            "ssh", "-i", self.ssh_key_path,
            f"{self.remote_user}@{self.instance_ip}",
            f"cd {self.remote_path} && docker-compose exec -T db pg_dump -U postgres skerritt_db > {backup_file}"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Database backed up to {backup_file}")
            return True
        else:
            print(f"⚠️  Backup failed: {result.stderr}")
            return False
    
    def check_deployment(self):
        """Check if deployment was successful"""
        print("\n🔍 Checking deployment status...")
        
        # Check if site is responding
        import requests
        try:
            response = requests.get(f"http://{self.instance_ip}", timeout=10)
            if response.status_code == 200:
                print(f"✅ Site is responding (Status: {response.status_code})")
            else:
                print(f"⚠️  Site returned status: {response.status_code}")
        except Exception as e:
            print(f"⚠️  Could not reach site: {e}")
        
        # Check Docker containers if using Docker
        cmd = [
            "ssh", "-i", self.ssh_key_path,
            f"{self.remote_user}@{self.instance_ip}",
            "docker ps --format 'table {{.Names}}\t{{.Status}}'"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("\n📊 Container Status:")
            print(result.stdout)
    
    def run(self, deployment_type='docker', backup=True):
        """Main deployment process"""
        print("🚀 Starting AWS Deployment Process")
        print("=" * 60)
        
        # Check AWS CLI
        if not self.check_aws_cli():
            return False
        
        # Select instance
        if not self.instance_ip:
            if not self.select_instance():
                return False
        
        # Test SSH
        if not self.test_ssh_connection():
            return False
        
        # Backup if requested
        if backup:
            self.backup_database()
        
        # Deploy
        if deployment_type == 'docker':
            self.deploy_with_docker()
        else:
            self.deploy_with_git()
        
        # Check deployment
        self.check_deployment()
        
        print("\n✅ Deployment complete!")
        print(f"🌐 Visit: http://{self.instance_ip}")
        
        return True

def main():
    parser = argparse.ArgumentParser(description='Deploy Skerritt Economics to AWS')
    parser.add_argument('--instance', help='Instance name or IP address')
    parser.add_argument('--type', choices=['docker', 'git'], default='docker',
                       help='Deployment type (default: docker)')
    parser.add_argument('--no-backup', action='store_true',
                       help='Skip database backup')
    parser.add_argument('--key', help='Path to SSH key file')
    
    args = parser.parse_args()
    
    deployer = AWSDeployer(instance_ip=args.instance)
    
    if args.key:
        deployer.ssh_key_path = args.key
    
    success = deployer.run(
        deployment_type=args.type,
        backup=not args.no_backup
    )
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()