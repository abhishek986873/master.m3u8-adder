import pyperclip
import time

link_count = 0

while True:
    current_clipboard = pyperclip.paste()
    time.sleep(1)  # wait for a short period of time to check the clipboard again

    if current_clipboard != pyperclip.paste():  # check if the clipboard has been updated
        link_count += 1
        link = pyperclip.paste() # get the link from the clipboard
        if "dash" in link:
            link = link.split("dash")[0] + "master.m3u8" # replace all words after "dash" with "master.m3u8"
        pyperclip.copy(link) # copy the updated link back to the clipboard
        print(f"Link {link_count}: {link}") # print the updated link with the index

    if pyperclip.paste().lower() == "exit":  # check if the clipboard contains "exit" to quit the program
        break

print("Exiting...")
