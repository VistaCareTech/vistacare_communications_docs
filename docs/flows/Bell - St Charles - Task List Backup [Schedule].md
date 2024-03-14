## Bell - St Charles - Task List Backup [Schedule]

### Description (What the workflow does?)
Daily saves the information contained in the Task List in an Excel spreadsheet located in [/Shared Documents/Backup](https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/StCharles/ElH9AaTWHopImN8vPjMknOIB9QoHmYEQ4KhiSmpveaxM9Q?e=QUhLcU) on the [Bell/St Charles](https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/default.aspx) subsite.

### How can you start the workflow? (Trigger Action)
Flow is automatically activated daily at 1 AM.

### Which are the decision points?
- Condition
    - "expression": {"greater": ["@length(outputs('Get_files_(properties_only)')?['body/value'])",30]}
    - Condition used to control the maximum number of backups kept in the directory.
    - If there are more than 30 versions of the backup saved in that directory, then the oldest version is deleted to free up space for the most recent version.

### How does the workflow end?
- Create an Excel file in the [/Shared Documents/Backup](https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/StCharles/ElH9AaTWHopImN8vPjMknOIB9QoHmYEQ4KhiSmpveaxM9Q?e=QUhLcU) folder

### What SharePoint lists are going to be affected by the workflow?
- [Task List](https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Tasks/1000%20Tasks.aspx)

### What excel spreadsheets are involved in the process?
- [TaskList_YYYY-MM-DDTHH_MM_SS.xlsx](https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/StCharles/ElH9AaTWHopImN8vPjMknOIB9QoHmYEQ4KhiSmpveaxM9Q?e=QUhLcU)
- The names of Excel spreadsheets are generated automatically taking into account the date and time.

### Video to GIF (Example of execution)