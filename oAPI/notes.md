###Primary Problem (1/2):
OMRA member registration/ renewal process is time consuming, manually managed process

###Challenge:
Create an app that fully automates the OMRA membership registration/ renewal process and allows 
access via an interface that allows for member data editing.
    
###Problem Validation:
##### 1. Steps in the current registration/ renewal process (1 of 2):
1. Take order and payment: handled by the site (squarespace), which is the OMRA site
2. Send digital membership card via email (manual)
3. Search member database to determine if the new user is a current member or 
a new member (based on what criteria, first and last name)
    - If the user IS NOT matched with any member in the database a new member record is created
    - If the user IS matched with a member in the DB the profile of that member is updated (address, phone, etc..)..

##### 2. Allow for member data update via easily understood interface (2 of 2):
1. Search for member via (insert criteria here)
2. Access/ read data of that member
3. Update the data for that user instance
4. Save the updated data
5. Return to the main search interface
asdlfk

###Secondary Problem (2/2):
Occurrence of human error in the series/ race scoring process

###Challenge:
Create an easily understood interface that is allows race results to be entered and edited and reduce 
the need of manual score entry and score calculations.
    
###Problem Validation:
##### 1. Scoring process:
- What data will be entered/ saved per SERIES?
- What data will be entered/ saved per RACE?
- Should the none racer position data be saved?
- Are all races in all series structured the same?

######Players:
    New Users (register users as member)
    Administrators (OMRA Staff)
######Steps:
    New Users:
        1. Register and Pay on OMRA squarespace site
        2. Data to be added or updated in the DB
        3. Email digital membership card to the new member
    
    Administrators (OMRA Staff):
        1. Enter the race results into database, via interface
        2. Edit race results if needed    