# Creating junk.fat Files

## Overview
Create a `junk.fat` file in your project directory to specify files and folders for deletion.

## File Format
List one item per line using relative paths:
```
temp_file.txt
build/
node_modules/
*.log
```

## Platform Instructions

### Windows
**Command Prompt:**
```cmd
echo temp_file.txt > junk.fat
echo build/ >> junk.fat
```

**PowerShell:**
```powershell
"temp_file.txt", "build/" | Out-File -FilePath junk.fat -Encoding utf8
```

**Notepad:**
```
notepad junk.fat
```

### Linux/Mac
**Terminal:**
```bash
cat > junk.fat << EOF
temp_file.txt
build/
EOF
```

**Text Editor:**
```bash
nano junk.fat
# or
vim junk.fat
```

## Path Rules
- Use relative paths (no leading `/`)
- Files: `filename.ext`
- Directories: `dirname/`
- Wildcards: `*.log`, `temp*`

## Usage
```bash
cd your-project
# Create junk.fat file
junk
```
