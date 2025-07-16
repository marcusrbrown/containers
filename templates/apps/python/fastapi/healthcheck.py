#!/usr/bin/env python3
"""
Health check script for {{ app_name }}

Verifies that the application is running and responsive.
"""

import requests
import sys
import os

def check_health():
    """Check application health."""
    try:
        port = os.getenv('PORT', '{{ port }}')
        response = requests.get(f'http://localhost:{port}/health', timeout=5)

        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'healthy':
                print("Health check passed")
                return True

        print(f"Health check failed: HTTP {response.status_code}")
        return False

    except requests.exceptions.RequestException as e:
        print(f"Health check failed: {e}")
        return False

if __name__ == "__main__":
    if check_health():
        sys.exit(0)
    else:
        sys.exit(1)
