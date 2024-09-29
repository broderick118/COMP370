1. Using the following commands:
    wc -l dialog.csv
    head dialog.csv
   we find that the dataset contains 36859 entries

2. Using the command: head dialog.csv
   we find that the data is organized into 4 columns: title, writer, pony, dialog

3. Run the command:
    grep -Eo "^\"[^\"]+" dialog.csv | sort --unique | wc -l
   which returns 198 lines, subtract one for the "title" line so 197 episodes

4. The character title "Others is nearly impossible to use grep to match with, since its contextual meaning requires a case-by case analysis by a real person, and the fact that it appears nearly 1000 times is far too much to do by hand.