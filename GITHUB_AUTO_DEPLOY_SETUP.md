# GitHub Auto-Deployment Setup for AWS Lightsail

This guide will set up automatic deployment from GitHub to your AWS Lightsail instance whenever you push to the main branch.

## Prerequisites
- AWS Lightsail instance already running
- SSH access to your Lightsail instance
- GitHub repository

## Step 1: Set Up GitHub Secrets

Go to your GitHub repository → Settings → Secrets and variables → Actions

Add these secrets:

1. **LIGHTSAIL_HOST**: Your Lightsail instance IP address
   - Example: `54.123.45.67`

2. **LIGHTSAIL_USERNAME**: SSH username (usually `ubuntu` or `ec2-user`)
   - Example: `ubuntu`

3. **LIGHTSAIL_KEY**: Your private SSH key content
   - Get it from your local machine:
     ```bash
     cat ~/.ssh/LightsailDefaultKey-us-east-1.pem
     ```
   - Copy the ENTIRE content including:
     ```
     -----BEGIN RSA PRIVATE KEY-----
     [key content]
     -----END RSA PRIVATE KEY-----
     ```

4. **LIGHTSAIL_PORT** (Optional): SSH port if not 22
   - Default: `22`

5. **SITE_URL** (Optional): Your website URL for verification
   - Example: `https://skerritteconomics.com`

## Step 2: Prepare Lightsail Instance

SSH into your Lightsail instance and run:

```bash
# 1. Ensure git repository is set up
cd /opt/skerritt-economics
git remote -v  # Should show your GitHub repo

# 2. Set up git to pull without password
git config credential.helper store
git config pull.rebase false

# 3. Copy the deployment script
sudo nano /opt/skerritt-economics/deploy.sh
# Paste the content from lightsail_auto_deploy.sh

# 4. Make it executable
chmod +x /opt/skerritt-economics/deploy.sh

# 5. Ensure proper permissions
sudo chown -R ubuntu:ubuntu /opt/skerritt-economics
```

## Step 3: Test Manual Deployment

On your Lightsail instance:

```bash
cd /opt/skerritt-economics
./deploy.sh
```

This should pull the latest code and restart services.

## Step 4: Enable GitHub Actions

1. The workflow file is already created at `.github/workflows/deploy.yml`
2. Commit and push it to GitHub:
   ```bash
   git add .github/workflows/deploy.yml
   git add lightsail_auto_deploy.sh
   git add GITHUB_AUTO_DEPLOY_SETUP.md
   git commit -m "Add GitHub Actions auto-deployment workflow"
   git push origin main
   ```

## Step 5: Test Auto-Deployment

1. Go to GitHub → Actions tab
2. You should see the "Deploy to AWS Lightsail" workflow
3. It will run automatically on push to main
4. You can also trigger it manually:
   - Click on the workflow
   - Click "Run workflow"
   - Select main branch
   - Click "Run workflow"

## How It Works

1. **Push to GitHub**: When you push code to the main branch
2. **GitHub Actions triggers**: The workflow starts automatically
3. **SSH to Lightsail**: GitHub Actions SSHs into your instance
4. **Pull and Deploy**: The instance pulls the latest code and restarts services
5. **Verification**: The workflow checks if the site is still running

## Monitoring Deployments

### On GitHub:
- Go to Actions tab to see deployment history
- Each deployment shows:
  - ✅ Success or ❌ Failure
  - Deployment logs
  - Time taken

### On Lightsail:
- Check deployment logs:
  ```bash
  tail -f /var/log/deploy.log
  ```
- Check service status:
  ```bash
  docker-compose ps  # If using Docker
  sudo systemctl status gunicorn  # If using Gunicorn
  ```

## Troubleshooting

### SSH Key Issues:
- Ensure the SSH key in GitHub secrets is complete
- Check key permissions on Lightsail (should be 600)
- Verify the username matches your instance

### Permission Issues:
```bash
# Fix permissions on Lightsail
sudo chown -R ubuntu:ubuntu /opt/skerritt-economics
sudo chmod -R 755 /opt/skerritt-economics
```

### Git Issues:
```bash
# Reset to clean state on Lightsail
cd /opt/skerritt-economics
git fetch origin
git reset --hard origin/main
```

### Service Won't Start:
```bash
# Check logs
docker-compose logs  # For Docker
journalctl -u gunicorn  # For Gunicorn
tail -f /var/log/nginx/error.log  # For Nginx
```

## Security Best Practices

1. **Use GitHub Secrets**: Never commit credentials
2. **Restrict SSH**: Use security groups to limit SSH access
3. **Monitor Actions**: Review deployment logs regularly
4. **Backup Before Deploy**: Consider adding backup step
5. **Use Branch Protection**: Require reviews before merging to main

## Optional Enhancements

### Add Slack/Email Notifications:
Edit `.github/workflows/deploy.yml` to add:
```yaml
- name: Send notification
  if: always()
  run: |
    curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
      -H 'Content-Type: application/json' \
      -d '{"text":"Deployment ${{ job.status }}"}'
```

### Add Health Checks:
```yaml
- name: Health check
  run: |
    for i in {1..5}; do
      if curl -f ${{ secrets.SITE_URL }}/health; then
        echo "Health check passed"
        break
      fi
      sleep 10
    done
```

### Add Rollback on Failure:
```yaml
- name: Rollback on failure
  if: failure()
  run: |
    ssh -i lightsail_key ${{ secrets.LIGHTSAIL_USERNAME }}@${{ secrets.LIGHTSAIL_HOST }} \
      "cd /opt/skerritt-economics && git reset --hard HEAD~1 && ./deploy.sh"
```

## Summary

After setup, your workflow will be:
1. Make changes locally
2. Commit and push to GitHub
3. Auto-deployment triggers
4. Site updates automatically in ~2-3 minutes
5. Check GitHub Actions for deployment status

No manual SSH or deployment needed!