#!/usr/bin/env python
"""
Generate a secure Django SECRET_KEY for production use.
Run this script to generate a new secret key for your .env file.
"""

from django.core.management.utils import get_random_secret_key

if __name__ == "__main__":
    print("\n" + "="*60)
    print("Django SECRET_KEY Generator")
    print("="*60)
    
    secret_key = get_random_secret_key()
    
    print("\nYour new SECRET_KEY:")
    print("-" * 60)
    print(secret_key)
    print("-" * 60)
    
    print("\nTo use this key:")
    print("1. Copy the key above")
    print("2. Add it to your .env file as:")
    print(f"   DJANGO_SECRET_KEY={secret_key}")
    print("\nNEVER commit this key to version control!")
    print("="*60 + "\n")