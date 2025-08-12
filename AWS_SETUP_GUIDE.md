# AWS CLI Setup and Deployment Guide

## Prerequisites
- AWS Account
- AWS CLI installed (already installed: v2.25.8)
- Access to AWS Lightsail or EC2

## Step 1: Configure AWS Credentials

### Option A: Using AWS Access Keys (Recommended for automation)

1. **Create IAM User and Access Keys:**
   - Log into AWS Console
   - Go to IAM → Users → Add User
   - User name: `skerritt-deploy`
   - Access type: Programmatic access
   - Attach policies:
     - `AmazonLightsailFullAccess` (for Lightsail)
     - `AmazonEC2FullAccess` (for EC2)
     - `AmazonS3FullAccess` (if using S3 for static files)

2. **Configure AWS CLI:**
   ```bash
   aws configure
   ```
   Enter when prompted:
   - AWS Access Key ID: [your-access-key]
   - AWS Secret Access Key: [your-secret-key]
   - Default region name: us-east-1 (or your preferred region)
   - Default output format: json

### Option B: Using AWS SSO (More secure for organizations)
```bash
aws configure sso
```

### Option C: Using Environment Variables
```bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-east-1"
```

## Step 2: Test AWS Connection

```bash
# Test Lightsail access
aws lightsail get-instances

# Test EC2 access (if using EC2)
aws ec2 describe-instances
```

## Step 3: Instance Information

### Current Setup Options:

#### Option 1: AWS Lightsail (Recommended for simplicity)
- Instance type: 2 GB RAM, 1 vCPU, 60 GB SSD
- Monthly cost: ~$10-20
- Pre-configured with Ubuntu 22.04

#### Option 2: AWS EC2
- Instance type: t3.small or t3.medium
- More flexible but requires more configuration

## Step 4: Deployment Methods

### Method 1: Direct SSH Deployment
```bash
# Deploy using existing scripts
./deploy_production.sh
```

### Method 2: Docker Deployment (Recommended)
```bash
# Build and push to instance
docker build -t skerritt-economics .
docker save skerritt-economics | ssh ubuntu@[instance-ip] docker load
```

### Method 3: AWS CLI Deployment Script
Use the automated deployment script created below.

## Security Notes

1. **Never commit AWS credentials to Git**
2. **Use IAM roles when possible**
3. **Rotate access keys regularly**
4. **Enable MFA on AWS account**
5. **Use least privilege principle for IAM policies**

## Environment Variables for Production

Create `.env.production` file:
```
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=skerritteconomics.com,www.skerritteconomics.com
DATABASE_URL=postgresql://user:pass@host:5432/dbname
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=skerritt-static
```

## Next Steps

After configuring AWS CLI:
1. Run `aws lightsail get-instances` to verify connection
2. Use deployment scripts to deploy updates
3. Set up automated CI/CD with GitHub Actions (optional)