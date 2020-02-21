#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Andrew Yeo, 2020-Feb-18, First Iteration of Fixing the Script)
# Andrew yeo, 2020-Feb-18, Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {}
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id': int(lstRow[0]), 'CD Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        pass
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': intID, 'CD Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
    
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        # This part displays the current inventory for the user to be able to see what they can delte 
        print('Your current inventory is...') 
        print('ID, CD Title, Artist') 
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        
        # This part prompts the user to an ID to delete
        delID = input('Enter an ID, CD, or Artist to delete: ') 
        
        # This part loops through all of the rows of the inventory "lstTbl"
        for i in range(len(lstTbl)): 
                if lstTbl[i]['id'] == int(delID): # If condition is triggered if the key of dictionary 'ID' matches what user has inputted
                    del lstTbl[i]  # Deletes that row
#                elif lstTbl[i]['CD Title'] == delID: # If condition is triggered if the key of dictionary 'ID' matches what user has inputted
#                    del lstTbl[i]  # Deletes that row
#                elif lstTbl[i]['Artist'] == delID: # If condition is triggered if the key of dictionary 'ID' matches what user has inputted
#                    del lstTbl[i]  # Deletes that row
                break
            
        # This part displays the inventory after the user has deleted the entry
        print('Your current inventory is now')  
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        pass
    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

