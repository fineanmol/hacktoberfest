import os, shutil

filetypes = [".png", ".jpg", ".mp3", ".pdf"]

path_from = input("Enter path location for where to move from: ").strip()
path_to = input("Enter path location for where to move to: ").strip()

filetype = input(f"Enter a filetype from {filetypes}: ").lower().strip()

# Check filetype validity
while filetype not in filetypes:
    print(f"❌ '{filetype}' is not supported. Choose from {filetypes}")
    filetype = input("Enter a valid filetype: ").lower().strip()

# Move files
count = 0
for file in os.listdir(path_from):
    if file.endswith(filetype):
        shutil.move(os.path.join(path_from, file), os.path.join(path_to, file))
        print(f"✅ Moved: {file}")
        count += 1

if count == 0:
    print("No files found with that type.")
else:
    print(f"🎉 Done! {count} file(s) moved.")
