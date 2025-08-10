#!/bin/bash

# AWS Lightsail instance setup script
# Run this on a fresh Ubuntu 22.04 Lightsail instance

set -e

echo "🔧 Setting up AWS Lightsail instance for Skerritt Economics..."

# Update system
echo "📦 Updating system packages..."
sudo apt-get update
sudo apt-get upgrade -y

# Install Docker
echo "🐳 Installing Docker..."
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Install Docker Compose
echo "🎼 Installing Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Add current user to docker group
sudo usermod -aG docker $USER

# Install Git
echo "📚 Installing Git..."
sudo apt-get install -y git

# Create app directory
echo "📁 Creating application directory..."
sudo mkdir -p /opt/skerritt-economics
sudo chown $USER:$USER /opt/skerritt-economics

# Clone repository (replace with your actual repo)
echo "📥 Cloning repository..."
cd /opt/skerritt-economics
# git clone https://github.com/yourusername/skerritt-economics.git .

# Create .env file
echo "🔐 Creating .env file..."
cat > .env.example << 'EOF'
# Copy this to .env and update with your values
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=generate-a-strong-secret-key-here
DJANGO_ALLOWED_HOSTS=your-domain.com,www.your-domain.com
EOF

# Create persistent data directory
echo "💾 Creating persistent data directory..."
mkdir -p /opt/skerritt-economics/data/db
mkdir -p /opt/skerritt-economics/data/media
mkdir -p /opt/skerritt-economics/data/static

# Set up firewall
echo "🔥 Configuring firewall..."
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw --force enable

# Install monitoring tools
echo "📊 Installing monitoring tools..."
sudo apt-get install -y htop ncdu

# Create systemd service for auto-start
echo "🚀 Creating systemd service..."
sudo tee /etc/systemd/system/skerritt-economics.service > /dev/null << 'EOF'
[Unit]
Description=Skerritt Economics Django Application
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/skerritt-economics
ExecStart=/usr/local/bin/docker-compose up -d
ExecStop=/usr/local/bin/docker-compose down
User=ubuntu
Group=docker

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable skerritt-economics

echo "✅ Lightsail setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Copy your application files to /opt/skerritt-economics"
echo "2. Copy .env.example to .env and update values"
echo "3. Run: cd /opt/skerritt-economics && ./deploy.sh"
echo "4. Configure your domain DNS to point to this server's IP"
echo ""
echo "⚠️  IMPORTANT: Log out and back in for Docker group changes to take effect"