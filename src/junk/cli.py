
"""
Junk CLI - Automated cleanup of unwanted files based on junk.fat
"""

import sys


def main():
    """Main entry point for the junk CLI tool."""
    try:

        from .cleanup import clean_up
        
        success = clean_up()
        if success:
            sys.exit(0)
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
